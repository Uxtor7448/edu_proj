def calculate_total(order) -> float:
    if not order.lines:
        raise EmptyOrderError("Order has no lines")
    return sum(line.subtotal() for line in order.lines)
