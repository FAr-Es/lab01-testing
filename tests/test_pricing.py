"""Lab 1: write your test functions here. Derive every expected value from L1-L2."""
import pytest

from tickets.pricing import ticket_price


def test_example_adult_without_card_pays_full_price():
    assert ticket_price(30, False) == 1000

def test_child_pays_500():
    assert ticket_price(12, False) == 500   


def test_adult_student_pays_800():
    assert ticket_price(30, True) == 800


def test_first_senior_pays_600():
    assert ticket_price(65, False) == 600   


def test_rejected_age_raises_value_error():
    with pytest.raises(ValueError):
        ticket_price(-1, False)
    with pytest.raises(ValueError):
        ticket_price(121, False)