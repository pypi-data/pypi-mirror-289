@pytest.mark.parametrize("expected, test_input", [
    (units.SYSTEM["MASS"], "mass"),
    (units.SYSTEM["TIME"], "time"),
    (units.SYSTEM["LENGTH"], "position"),
    (units.SYSTEM["CHARGE"], "charge"),
    (units.SYSTEM["LENGTH"] / units.SYSTEM["TIME"], "velocity")
])
def test_H5MD_units(open_file, expected, test_input):
    """Tests that all units in the H5MD file are stored as expected
    """
    h5md_read = H5MD_reader.read_units(open_file, test_input)
    assert str(expected) == h5md_read
