from dataclasses import dataclass, field

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
    lines: list = field(default_factory=list)
