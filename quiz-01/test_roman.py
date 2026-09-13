from roman import roman_to_number, validate_roman_rules

def test_roman_to_number_calculations():
    assert roman_to_number("I") == 1
    assert roman_to_number("IV") == 4
    assert roman_to_number("IX") == 9
    assert roman_to_number("XIV") == 14
    assert roman_to_number("MCMXCIV") == 1994

def test_validation_success():
    is_valid, msg = validate_roman_rules("XIV")
    assert is_valid is True
    assert msg == ""

def test_validation_success():
    is_valid, msg = validate_roman_rules("MMVI")
    assert is_valid is True
    assert msg == ""

def test_validation_vld_repetition():
    is_valid, msg = validate_roman_rules("VV")
    assert is_valid is False
    assert "Symbols V, L, and D cannot be repeated" in msg

def test_validation_ixcm_repetition():
    is_valid, msg = validate_roman_rules("IIII")
    assert is_valid is False
    assert "cannot be repeated more than 3 times" in msg

def test_validation_vld_subtraction():
    is_valid, msg = validate_roman_rules("VX")
    assert is_valid is False
    assert "cannot be placed in front of a larger symbol" in msg

def test_validation_i_subtraction_rules():
    is_valid, msg = validate_roman_rules("IL")
    assert is_valid is False
    assert "'I' can only be subtracted from 'V' or 'X'" in msg

def test_validation_x_subtraction_rules():
    is_valid, msg = validate_roman_rules("XD")
    assert is_valid is False
    assert "'X' can only be subtracted from 'L' or 'C'" in msg

def test_validation_c_subtraction_valid():
    # C can validly precede M or D (e.g., CM = 900)
    is_valid, msg = validate_roman_rules("CM")
    assert is_valid is True
    assert msg == ""