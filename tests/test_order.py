import pytest
from src.order.models import Order, OrderLine
from src.order.service import calculate_total
from src.order.exceptions import EmptyOrderError, InvalidQuantityError


def test_calculate_total_ok():
    order = Order(id="1", lines=[OrderLine("p1", 2, 100.0)])
    assert calculate_total(order) == 200.0


def test_calculate_total_empty_raises():
    with pytest.raises(EmptyOrderError):
        calculate_total(Order(id="1"))


def test_invalid_quantity_zero():
    with pytest.raises(InvalidQuantityError):
        from src.order.service import validate_line
        validate_line(OrderLine("p1", 0, 100.0))


def test_invalid_quantity_negative():
    with pytest.raises(InvalidQuantityError):
        from src.order.service import validate_line
        validate_line(OrderLine("p1", -1, 100.0))


def test_calculate_total_multiple_lines():
    order = Order(id="1", lines=[
        OrderLine("p1", 2, 100.0),
        OrderLine("p2", 1, 50.0),
    ])
    assert calculate_total(order) == 250.0
