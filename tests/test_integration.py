import pytest
from src.catalog.catalog import Catalog
from src.catalog.port import Product
from src.order.service import create_order, calculate_total
from src.order.exceptions import ProductNotFoundError, InsufficientStockError


def test_create_order_success():
    c = Catalog()
    c.add_product(Product("p1", "Keyboard", 100.0, 10))
    order = create_order("o1", [("p1", 2)], c)
    assert calculate_total(order) == 200.0


def test_create_order_product_not_found():
    c = Catalog()
    with pytest.raises(ProductNotFoundError):
        create_order("o1", [("nope", 1)], c)


def test_create_order_insufficient_stock():
    c = Catalog()
    c.add_product(Product("p1", "Keyboard", 100.0, 1))
    with pytest.raises(InsufficientStockError):
        create_order("o1", [("p1", 5)], c)


def test_create_order_invalid_quantity():
    c = Catalog()
    c.add_product(Product("p1", "Keyboard", 100.0, 10))
    from src.order.exceptions import InvalidQuantityError
    with pytest.raises(InvalidQuantityError):
        create_order("o1", [("p1", 0)], c)
