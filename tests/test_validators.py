import pytest

from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert get_issuer("4353 2343 2342 4321") == "Visa"
    with pytest.raises(ValueError):
        get_issuer("7353 2343 2342 4321")

def test_get_issuer_master_card():
    assert get_issuer("5532 2131 3211 2321") == "MasterCard"
    assert get_issuer("5332 2131 3211 2321") == "MasterCard"
    with pytest.raises(ValueError):
        get_issuer("5632 2131 3211 2321")

def test_get_issuer_american_express():
    assert get_issuer("3734 3212 3211 234") == "American Express"
    assert get_issuer("3434 3212 3211 234") == "American Express"
    with pytest.raises(ValueError):
        get_issuer("3334 3212 3211 234")

def test_length():
    with pytest.raises(ValueError):
        get_issuer("4353 2343 2342 4321 1")
    with pytest.raises(ValueError):
        get_issuer("4353 2343 2342 432")
    with pytest.raises(ValueError):
        get_issuer("5532 2131 3211 2323 3")
    with pytest.raises(ValueError):
        get_issuer("5532 2131 3211 232")
    with pytest.raises(ValueError):
        get_issuer("3734 3212 3211 2344")
    with pytest.raises(ValueError):
        get_issuer("3734 3212 3211 23")
