import json
from pathlib import Path
from ..order.models import Order, OrderLine


class StorageError(Exception):
    pass


class Storage:
    def __init__(self, path: str = "orders.json"):
        self.path = Path(path)

    def save(self, order: Order) -> None:
        try:
            data = self._load_all()
            data[order.id] = {
                "id": order.id,
                "status": order.status,
                "lines": [
                    {
                        "product_id": l.product_id,
                        "quantity": l.quantity,
                        "unit_price": l.unit_price,
                    }
                    for l in order.lines
                ],
            }
            self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except OSError as e:
            raise StorageError(f"Failed to save order: {e}")

    def load(self, order_id: str) -> Order:
        data = self._load_all()
        if order_id not in data:
            raise StorageError(f"Order {order_id} not found")
        raw = data[order_id]
        order = Order(id=raw["id"], status=raw["status"])
        for line in raw["lines"]:
            order.add_line(OrderLine(**line))
        return order

    def _load_all(self) -> dict:
        if not self.path.exists():
            return {}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            raise StorageError(f"Failed to read storage: {e}")
