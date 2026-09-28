from typing import List, Optional
from .port import CatalogPort, Product


class ProductNotFoundError(Exception):
    pass


class Catalog(CatalogPort):
    def __init__(self):
        self._products: dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        self._products[product.product_id] = product

    def get_product(self, product_id: str) -> Optional[Product]:
        return self._products.get(product_id)

    def check_availability(self, product_id: str, qty: int) -> bool:
        product = self._products.get(product_id)
        if product is None:
            return False
        return product.quantity >= qty

    def list_products(self) -> List[Product]:
        return list(self._products.values())
