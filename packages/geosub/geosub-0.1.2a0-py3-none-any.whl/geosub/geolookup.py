import os
import re
from typing import Optional


# Self-documenting type aliases
CountryCode = str
PostalCode = str
SubdivisionCode = str
SubdivisionName = str
Subdivision = tuple[SubdivisionCode, SubdivisionName]


class SubdivisionCodeLookup:
    def __init__(self, postal_code_data_file: str):
        """
        This class enables looking up a ISO 3166-2 subdivision code for a country and
        postal code prefix.

        The postal_code_data_file is sourced from:
        https://download.geonames.org/export/zip/?C=S;O=D

        By downloading allCountries.zip, extracting, and then sorting it into a new file.

        The data is licensed under a Creative Commons Attribution 4.0 License with
        credit to www.geonames.org.

        The data can be restributed provided credit is given to geonames
        (a link on your website to www.geonames.org is ok).

        See: http://creativecommons.org/licenses/by/4.0/

        Below is the file format info taken directly from URL above.

        The data format is tab-delimited text in utf8 encoding, with the following fields :

        country code      : iso country code, 2 characters
        postal code       : varchar(20)
        place name        : varchar(180)
        admin name1       : 1. order subdivision (state) varchar(100)
        admin code1       : 1. order subdivision (state) varchar(20)
        admin name2       : 2. order subdivision (county/province) varchar(100)
        admin code2       : 2. order subdivision (county/province) varchar(20)
        admin name3       : 3. order subdivision (community) varchar(100)
        admin code3       : 3. order subdivision (community) varchar(20)
        latitude          : estimated latitude (wgs84)
        longitude         : estimated longitude (wgs84)
        accuracy          : accuracy of lat/lng from 1=estimated, 4=geonameid,
        6=centroid of addresses or shape
        """
        self.postal_code_data_file = postal_code_data_file

    def find_subdivision(
        self,
        country: CountryCode,
        postal_code: PostalCode,
        allow_empty_prefix: bool = False,
    ) -> Optional[Subdivision]:
        """
        Attempts to find an ISO 3166-2 subdivision code for a given country code and postal code.

        Parameters:
            country (CountryCode): The ISO 3166-1 alpha-2 country code.
            postal_code (PostalCode): The postal code or postal code prefix.
            allow_empty_prefix (bool): Whether to allow an empty postal code prefix.

        Returns:
            Optional[Subdivision]: A tuple containing the subdivision code and name,
                                   or None if not found.

        Examples:
            >>> from geosub.geolookup import SubdivisionCodeLookup
            >>> lookup = SubdivisionCodeLookup("geosub/data/geonames_all_countries_sorted.tsv")

            >>> lookup.find_subdivision("US", "90210")
            ('CA', 'California')
        """
        country, prefix = _normalize_input(country, postal_code)

        if not country or (not prefix and not allow_empty_prefix):
            return None

        if not (record := self._search_record(target_key=(country, prefix))):
            return None

        subdivision_code = record[4]
        subdivision_name = _transliterate(record[3])
        subdivision_name = _clean_region_name(subdivision_name)

        if subdivision_code and subdivision_name:
            return subdivision_code, subdivision_name

        return None

    def _search_record(
        self,
        target_key: tuple[CountryCode, PostalCode],
    ) -> Optional[list[str]]:
        """
        Perform a binary search for geonames postal code data.

        Multiple records can match the same postal code, but we only return
        the first one found as its only an approximation.
        """
        statinfo = os.stat(self.postal_code_data_file)
        with open(self.postal_code_data_file, "rb") as file:
            filesize = statinfo.st_size
            low, high = 0, filesize

            while low < high:
                mid = (low + high) // 2
                file.seek(mid)
                file.readline()  # Skip partial line
                if not (line := file.readline()):
                    break  # Reached EOF

                parts = line.decode().split("\t")
                current_key = tuple(parts[:2])
                current_country, current_postcode = current_key
                target_country, target_postcode = target_key

                if current_key < target_key:
                    low = mid + 1
                elif (current_country > target_country) or (
                    current_postcode > target_postcode
                    and not current_postcode.startswith(target_postcode)
                ):
                    high = mid - 1
                else:
                    # Found an exact or prefix match
                    return parts

        return None


def _normalize_input(
    country: CountryCode,
    postal_code: PostalCode,
) -> tuple[CountryCode, PostalCode]:
    """
    Normalize the country code and postal code by stripping whitespace,
    uppercasing, and handling special cases for certain countries.

    Examples:
        >>> from geosub.geolookup import _normalize_input
        >>> _normalize_input("  us  ", "  90210  ")
        ('US', '9021')
        >>> _normalize_input("  Ca  ", "  K1A 0A0  ")
        ('CA', 'K1A')
    """
    country = country.strip().upper()
    prefix = postal_code.replace(" ", "")[:4].upper()

    if country in {"CA", "IE", "MT"}:
        prefix = prefix[:3]  # Special handling for Canada, Ireland, and Malta

    return country, prefix


def _clean_region_name(region_name: str) -> str:
    """
    Clean up a region name by removing any suffix enclosed in parentheses.

    Examples:
        >>> clean_region_name("Mayotte (general)")
        'Mayotte'
        >>> clean_region_name("Central Region (general)")
        'Central Region'
        >>> clean_region_name("Northern Area (specific)")
        'Northern Area'
        >>> clean_region_name("Southern Province (other)")
        'Southern Province'
        >>> clean_region_name("Circonscription d'Uvéa")
        'Uvéa'
        >>> clean_region_name("Circonscription de Sigave")
        'Sigave'
        >>> clean_region_name("Circonscription d'Alo")
        'Alo'
    """
    pattern = re.compile(r"\s*\(.*?\)$")
    cleaned_name = pattern.sub("", region_name)

    # Remove specific prefixes like "Circonscription d'" and "Circonscription de"
    pattern_prefix = re.compile(r"^Circonscription (d'|de)\s*")
    cleaned_name = pattern_prefix.sub("", cleaned_name)

    return cleaned_name.strip()


def _transliterate(text: str) -> str:
    """
    Transliterate Cyrillic characters to Latin characters.

    Source: https://stackoverflow.com/a/14173535

    Examples:
        >>> transliterate("Москва")
        'Moskva'
        >>> transliterate("Привет, мир!")
        'Privet, mir!'
    """
    symbols = (
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA",
    )

    translation_table = {ord(a): ord(b) for a, b in zip(*symbols)}

    return text.translate(translation_table)
