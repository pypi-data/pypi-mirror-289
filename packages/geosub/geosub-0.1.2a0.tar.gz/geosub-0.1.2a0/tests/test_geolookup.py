from typing import Optional
import pytest
from geosub.geolookup import SubdivisionCodeLookup


@pytest.mark.parametrize(
    "country_code,postal_code,expected_subdivision",
    [
        ("gb", "EC3N 4AB", ("ENG", "England")),
        ("gb", "foobar", None),
        ("UK", "EC3N 4AB", None),
        ("GB", "", None),
        ("", "", None),
        ("GB", "x", None),
        ("CA", "M5H 2N2", ("ON", "Ontario")),
        ("CA", "V6B 2Z4", ("BC", "British Columbia")),
        ("CA", "A1B 1C3", ("NL", "Newfoundland and Labrador")),
        ("AU", "6443", ("WA", "Western Australia")),
        ("NZ", "8013", ("E9", "Canterbury")),
        ("CN", "010000", ("20", "Inner Mongolia")),
        ("IN", "400001", ("16", "Maharashtra")),
        ("RU", "101000", ("48", "Moskva")),  # Moscow
        ("BR", "69000", ("04", "Amazonas")),  # Manaus, Amazonas
        ("FO", "FO-100", None),  # Faroe Islands have no subdivisions
        ("FO", "100", None),
        ("IS", "101", None),  # Missing subdivision data for Iceland
        ("GG", "GY1 1AA", None),  # No subdivision codes defined for Guernsey
        ("GF", "97300", ("GF", "Guyane")),  # French Guiana
        ("YT", "97600", ("00", "Mayotte")),  # Mayotte
        (
            "PF",
            "98714",
            ("01", "Îles du Vent"),
        ),  # Pape'ete in Windward Islands, French Polynesia
        ("WF", "98600", ("98613", "Uvéa")),  # Wallis and Futuna
    ],
)
def test_lookup(
    data_file_path: str,
    country_code: str,
    postal_code: str,
    expected_subdivision: Optional[tuple[str, str]],
):
    lookup = SubdivisionCodeLookup(data_file_path)
    assert lookup.find_subdivision(country_code, postal_code) == expected_subdivision
