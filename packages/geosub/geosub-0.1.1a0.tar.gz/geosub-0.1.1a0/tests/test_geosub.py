import pytest
import pycountry
import geosub


@pytest.mark.parametrize(
    "country_code,postal_code,expected_subdivision",
    [
        ("", "", None),
        ("GB", "SW1", "ENG"),  # England
        ("AU", "2000", "NSW"),  # New South Wales
        ("AU", "6000", "WA"),  # Western Australia
        ("CA", "M5H 2N2", "ON"),  # Ontario
        ("CA", "V6B 2Z4", "BC"),  # British Columbia
        ("IN", "400001", "MH"),  # Maharashtra
        ("RU", "101000", "MOW"),  # Moscow
        ("RU", "690091", "PRI"),  # Primorsky Krai
        ("BR", "01000-000", "SP"),  # São Paulo
        ("BR", "69000-000", "AM"),  # Amazonas
        ("AD", "AD500", "07"),  # Andorra la Vella
        ("LI", "9490", "11"),  # Vaduz
        ("FO", "FO-110", None),  # Faroe Islands don't have any subdivisions
        ("SM", "47890", None),  # San Marino is a microstate without subdivisions
        ("MC", "98000", "MO"),  # Monaco
        ("MT", "VLT 1112", "60"),  # Valletta, Malta
        ("IE", "D02 CK83", "L"),  # Leinster, where Dublin is located.
        ("LU", "L-1313", "LU"),  # Luxembourg
        ("IS", "101", None),  # Missing data for Iceland's subdivisions
        ("GG", "GY1 1AA", None),  # No subdivisions for Guernsey
        ("GI", "GX11 1AA", None),  # No data for Gibraltar
        ("NP", "44600", None),  # No data for Nepal
        (
            "IN",
            "110001",
            "DL",
        ),  # Delhi, a union territory serving also as a subdivision.
        ("IR", "11369", None),  # No data for Iran
        ("CA", "A1B 1C3", "NL"),  # Newfoundland and Labrador
        ("AU", "6443", "WA"),  # Western Australia
        ("NZ", "8013", "CAN"),  # Canterbury region
        ("VE", "1010", None),  # No data for Venezuela
        ("MM", "11181", None),  # No data for Myanmar
        ("AF", "1001", None),  # No data for Afghanistan
        ("WS", "96799", None),  # No data for Samoa
        ("EG", "11511", None),  # No data for Egypt
        ("CN", "100000", "BJ"),  # Beijing Municipality
        ("KE", "00100", None),  # No data for Kenya
        ("NG", "101001", None),  # No data for Nigeria
        ("VN", "100000", None),  # No data for Vietnam
        ("SA", "11564", None),  # No data for Saudi Arabia
        ("MA", "20000", None),  # Missing postal code data for Casablanca-Settat
        ("MA", "22000", "05"),  # But we do have some postal code data for Fès-Meknès
        ("GH", "00233", None),  # No data for Ghana
        ("ZW", "H001", None),  # No data for Zimbabwe
        ("UZ", "110100", None),  # No data for Uzbekistan
        ("FR", "75001", "11"),  # Île-de-France, the region for Paris
        # Pycountry uses FR in the code as French Guiana is a department of France
        # even though GF is the country code
        (
            "GF",
            "97300",
            "FR-973",
        ),
        (
            "GP",
            "97100",
            "FR-971",
        ),  # Guadeloupe is treated similarly to French Guiana
        ("MQ", "97200", "FR-972"),  # Martinique, same as above
        ("RE", "97400", "FR-974"),  # Réunion, same as above
        ("YT", "97600", "FR-976"),  # Mayotte, same as above
        ("PM", "97500", "FR-PM"),  # Saint Pierre and Miquelon, same as above
        ("BL", "97133", None),  # No data for Saint Barthélemy
        ("MF", "97150", None),  # No data for Saint Martin
        (
            "PF",
            "98714",
            None,
        ),  # Can't find Pape'ete in Windward Islands, French Polynesia
        ("NC", "98800", None),  # Can't find info for this place in New Caledonia
        ("WF", "98600", "WF-UV"),  # Mata-Utu in Wallis, Wallis and Futuna
        ("US", "96815", "HI"),  # Honolulu, Hawaii
        ("US", "99501", "AK"),  # Anchorage, Alaska
        ("US", "98101", "WA"),  # Seattle, Washington
        ("US", "80202", "CO"),  # Denver, Colorado
        ("US", "60604", "IL"),  # Chicago, Illinois
        ("US", "10020", "NY"),  # New York City, New York
        ("US", "47591", "IN"),  # Vincennes, Indiana
        ("US", "62439", "IL"),  # Lawrenceville, Illinois
        ("US", "79855", "TX"),  # Kent, Texas
        ("US", "88220", "NM"),  # Carlsbad, New Mexico
        ("US", "58103", "ND"),  # Fargo, North Dakota
        ("US", "56560", "MN"),  # Moorhead, Minnesota
        ("US", "32565", "FL"),  # Jay, Florida
        ("US", "32401", "FL"),  # Panama City, Florida
        ("US", "32566", "FL"),  # Navarre, Florida
        ("US", "33131", "FL"),  # Miami, Florida
        ("US", "33602", "FL"),  # Tampa, Florida
        ("US", "32801", "FL"),  # Orlando, Florida
        ("AO", "1000", None),  # No data for Angola
        ("BJ", "0101", None),  # No data for Benin
        ("BO", "0001", None),  # No data for Bolivia
        ("FJ", "1000", None),  # No data for Fiji
        ("GA", "01", None),  # No data for Gabon
        ("LY", "1001", None),  # No data for Libya
        ("MW", "101", "N"),  # Lilongwe, Milawi
        ("SC", "0000", None),  # No data for Seychelles
        ("SB", "0000", None),  # No data for Solomon Islands
        ("AE", "00000", None),  # No data for United Arab Emirates
        ("AE", "99999", None),  # No data for United Arab Emirates
        ("HK", "000", None),  # No data for Hong Kong
        ("QA", "00000", None),  # No data for Qatar
        ("MO", "999078", None),  # No data for Macau
        ("ZZ", "12345", None),  # Non-existent country code
        ("US", "ABCDE", None),  # Invalid non-numeric zipcode
        ("", "", None),
        ("US", "1234567890", "NY"),  # Unusually long postal code
        ("123", "12345", None),  # Country code as numbers
        ("US", "!@#$%", None),  # Invalid characters in postal code
        (" US ", " 12345 ", "US-NY"),  # Leading and trailing whitespaces
        ("uS", "12345", "US-NY"),  # Country code in lower case
        ("CA", "A1A 1A1", "NL"),
        ("US", "123", "NY"),
        ("GB", "SW1A 1AA@", "ENG"),  # Postal code with special character
        ("U$", "12345", None),  # Invalid country code
        ("US", "47591", "IN"),
        ("US", "1234A", "NY"),
    ],
)
def test_lookup(country_code: str, postal_code: str, expected_subdivision: str):
    actual_subdivision = geosub.lookup(country_code, postal_code)
    if actual_subdivision is None or expected_subdivision is None:
        assert actual_subdivision is expected_subdivision is None
    else:
        assert actual_subdivision.code in [
            expected_subdivision,
            f"{country_code}-{expected_subdivision}",
        ]


def test_lookup_all_countries():
    supported_countries: list[str] = []
    unsupported_countries: list[str] = []

    for country in pycountry.countries:
        if geosub.lookup(country.alpha_2, "", allow_empty_prefix=True):
            supported_countries.append(country.alpha_2)
        else:
            unsupported_countries.append(country.alpha_2)

    assert supported_countries == geosub.SUPPORTED_COUNTRY_CODES
    assert [
        pycountry.countries.get(alpha_2=code).name for code in supported_countries
    ] == geosub.SUPPORTED_LOCATIONS
    assert unsupported_countries == geosub.UNSUPPORTED_COUNTRY_CODES
    assert [
        pycountry.countries.get(alpha_2=code).name for code in unsupported_countries
    ] == geosub.UNSUPPORTED_LOCATIONS
