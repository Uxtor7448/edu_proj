from .models import Order, OrderLine
from .exceptions import (
    EmptyOrderError,
    InvalidQuantityError,
    ProductNotFoundError,
    InsufficientStockError,
)
from ..catalog.port import CatalogPort


def calculate_total(order: Order) -> float:
    if not order.lines:
        raise EmptyOrderError("Order has no lines")
    return sum(line.subtotal() for line in order.lines)


def validate_line(line: OrderLine) -> None:
    if line.quantity <= 0:
        raise InvalidQuantityError(f"Quantity must be > 0, got {line.quantity}")
    if line.unit_price < 0:
        raise InvalidQuantityError(f"Price must be >= 0, got {line.unit_price}")


def create_order(order_id: str, items: list[tuple[str, int]], catalog: CatalogPort) -> Order:
    order = Order(id=order_id)
    for product_id, qty in items:
        if qty <= 0:
            raise InvalidQuantityError(f"Quantity must be > 0, got {qty}")

        product = catalog.get_product(product_id)
        if product is None:
            raise ProductNotFoundError(f"Product {product_id} not found")

        if not catalog.check_availability(product_id, qty):
            raise InsufficientStockError(
                f"Not enough stock for {product_id}: requested {qty}, available {product.quantity}"
            )

        line = OrderLine(product_id=product_id, quantity=qty, unit_price=product.price)
        validate_line(line)
        order.add_line(line)

    return order


def confirm_order(order: Order) -> Order:
    if order.status != "Draft":
        raise ValueError(f"Cannot confirm order in status {order.status}")
    if not order.lines:
        raise EmptyOrderError("Cannot confirm empty order")
    order.status = "Confirmed"
    return order


def pay_order(order: Order) -> Order:
    if order.status != "Confirmed":
        raise ValueError(f"Cannot pay order in status {order.status}")
    order.status = "Paid"
    return order


def cancel_order(order: Order) -> Order:
    if order.status in ("Paid", "Completed"):
        raise ValueError(f"Cannot cancel order in status {order.status}")
    order.status = "Cancelled"
    return order
