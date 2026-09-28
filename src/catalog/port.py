from abc import ABC, abstractmethod

class CatalogPort(ABC):
    @abstractmethod
    def get_product(self, product_id: str): ...
    @abstractmethod
    def check_availability(self, product_id: str, qty: int) -> bool: ...
