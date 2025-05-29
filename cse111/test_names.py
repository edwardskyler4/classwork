from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Johnny", "Roberts") == "Roberts; Johnny"
    assert make_full_name("Sarah", "Elbertson") == "Elbertson; Sarah"
    assert make_full_name("Chris", "Ellis") == "Ellis; Chris"

def test_extract_family_name():
    assert extract_family_name("Roberts; Johnny") == "Roberts"
    assert extract_family_name("Elbertson; Sarah") == "Elbertson"
    assert extract_family_name("Ellis; Chris") == "Ellis"

def test_extract_given_name():
    assert extract_given_name("Roberts; Johnny") == "Johnny"
    assert extract_given_name("Elbertson; Sarah") == "Sarah"
    assert extract_given_name("Ellis; Chris") == "Chris"



pytest.main(["-v", "--tb=line", "-rN", __file__])