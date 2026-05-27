import pytest
from src.discount import calculate_discount

#Here we can start our Equivalence Partitioning tests


def test_ep_small_purchase_non_member():
    assert calculate_discount(20.00, False) == 20.00

def test_ep_large_purchase_member():
    assert calculate_discount(100.00, True) == 85.50
    
def test_ep_invalid_purchase_raises():
    with pytest.raises(ValueError):
        calculate_discount(-10.00, False)
        
#Boundary Value Analysis (BVA) tests
def test_bva_just_below_threshold():
    assert calculate_discount(49.99, False) == 49.99

def test_bva_exactly_at_threshold():
    assert calculate_discount(50.00, False) == 45.00
    
def test_bva_zero_purchase():
    
    assert calculate_discount(0.00, False) == 0.00
    
