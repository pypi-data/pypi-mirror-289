from typing import Optional
from importlib.resources import files, as_file
import pycountry
from .geolookup import SubdivisionCodeLookup, CountryCode, PostalCode


def lookup(
    country_code: CountryCode,
    postal_code: PostalCode,
    allow_empty_prefix: bool = False,
) -> Optional[pycountry.SubdivisionHierarchy]:
    """
    Retrieves the ISO 3166-2 subdivision information for a given country code and postal code.

    This function searches an offline dataset to find the time zone associated with
    the specified postal code within a given country. It uses this to retrieve the subdivision
    information from the `pycountry` library, based on the input parameters. If
    no matching information is found, the function returns `None`.

    Parameters:
        country_code (str):         The ISO 3166-1 alpha-2 country code, a two-letter
                                    string that uniquely identifies the country.
        postal_code (str):          The postal code for the specified location within
                                    the country. The format and length can vary depending
                                    on the country. A prefix may be used. The shorter the
                                    prefix, the more potential geographic matches there
                                    could be. The first match will be used.
        allow_empty_prefix (bool):  Included for testing purposes and defaults to `False`.
                                    Setting it to true will allow an empty `postal_code`
                                    to be passed, which will match any postal code.

    Returns:
        Optional[SubdivisionHierarchy]: The pycountry `SubdivisionHierarchy` object, if
                                        one can be found.

    Examples:
        >>> geosub.lookup('US', '10001')
        SubdivisionHierarchy(code='US-NY', country_code='US', name='New York', ..., type='State')

        >>> geosub.lookup('CA', 'M5H 2N2')
        SubdivisionHierarchy(code='CA-ON', country_code='CA', name='Ontario',..., type='Province')
    """
    data_resource = files("geosub.data").joinpath("geonames_all_countries_sorted.tsv")
    with as_file(data_resource) as data_file_path:
        sublookup = SubdivisionCodeLookup(str(data_file_path))
        if (
            subdivision := sublookup.find_subdivision(
                country_code,
                postal_code,
                allow_empty_prefix,
            )
        ) is None:
            return None

        subdivision_code, subdivision_name = subdivision

        result: pycountry.SubdivisionHierarchy = pycountry.subdivisions.get(
            code=f"{country_code}-{subdivision_code}",
        )
        if result:
            return result

        results: Optional[list[type[pycountry.Subdivisions]]]
        try:
            results = pycountry.subdivisions.search_fuzzy(subdivision_name)
        except LookupError:
            results = None

        if results is None:
            return None

        if len(results) > 1:
            results = [
                r
                for r in results
                if not isinstance(r, pycountry.SubdivisionHierarchy)
                or r.country_code == country_code
            ]

        if len(results) == 1 and isinstance(results[0], pycountry.SubdivisionHierarchy):
            return results[0]

        return None
