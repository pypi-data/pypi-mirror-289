import pytest

from ldkex import Extractor


@pytest.fixture
def setup_extractor():
    extractor = Extractor()
    return extractor


@pytest.mark.parametrize("file_path, expected_geometries, expected_geometries_no_duplicates, "
                         "expected_points, expected_lines, expected_polygons", [
                             ('data/test_data-01.ldk', 242830, 23047, 234713, 6183, 1934),
                             ('data/test_data-02.ldk', 30932, 28203, 28258, 2368, 306),
                         ])
def test_extract_file(setup_extractor, file_path, expected_geometries, expected_geometries_no_duplicates,
                      expected_points, expected_lines, expected_polygons):
    extractor = setup_extractor
    with open(file_path, 'rb') as file:
        extractor.extract(file)
    assert len(extractor.geometries) == expected_geometries
    assert len(extractor.get_points()) == expected_points
    assert len(extractor.get_lines()) == expected_lines
    assert len(extractor.get_polygons()) == expected_polygons

    extractor.geometries.remove_duplicates(fields=['name', 'coordinates', 'outline_color'])
    assert len(extractor.geometries) == expected_geometries_no_duplicates
