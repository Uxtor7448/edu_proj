from abc import ABC, abstractmethod
from typing import List, Optional


class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.quantity})"


class CatalogPort(ABC):
    @abstractmethod
    def get_product(self, product_id: str) -> Optional[Product]:
        ...

    @abstractmethod
    def check_availability(self, product_id: str, qty: int) -> bool:
        ...

    @abstractmethod
    def list_products(self) -> List[Product]:
        ...
