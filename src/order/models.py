from dataclasses import dataclass, field
from typing import List


@dataclass
class OrderLine:
    product_id: str
    quantity: int
    unit_price: float

    def subtotal(self) -> float:
        return self.quantity * self.unit_price


@dataclass
class Order:
    id: str
    status: str = "Draft"
    lines: List[OrderLine] = field(default_factory=list)

    def add_line(self, line: OrderLine) -> None:
        self.lines.append(line)
