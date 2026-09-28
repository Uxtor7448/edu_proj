import pytest
from src.catalog.catalog import Catalog
from src.catalog.port import Product


def test_add_and_get_product():
    c = Catalog()
    c.add_product(Product("p1", "Keyboard", 100.0, 10))
    assert c.get_product("p1").name == "Keyboard"


def test_get_missing_product_returns_none():
    c = Catalog()
    assert c.get_product("nope") is None


def test_check_availability_true():
    c = Catalog()
    c.add_product(Product("p1", "Keyboard", 100.0, 10))
    assert c.check_availability("p1", 5) is True


def test_check_availability_false_when_not_enough():
    c = Catalog()
    c.add_product(Product("p1", "Keyboard", 100.0, 2))
    assert c.check_availability("p1", 5) is False


def test_negative_price_raises():
    with pytest.raises(ValueError):
        Product("p1", "Bad", -1.0, 1)
