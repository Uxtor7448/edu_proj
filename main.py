from src.catalog.catalog import Catalog
from src.catalog.port import Product
from src.order.service import create_order, calculate_total, confirm_order, pay_order
from src.storage.storage import Storage


def main():
    catalog = Catalog()
    catalog.add_product(Product("p1", "Keyboard", 100.0, 10))
    catalog.add_product(Product("p2", "Mouse", 50.0, 5))

    order = create_order("o1", [("p1", 2), ("p2", 1)], catalog)
    print(f"Order {order.id} created, status={order.status}")
    print(f"Total: {calculate_total(order)}")

    confirm_order(order)
    pay_order(order)
    print(f"Order status after payment: {order.status}")

    storage = Storage("orders.json")
    storage.save(order)
    print("Order saved.")

    loaded = storage.load("o1")
    print(f"Loaded order {loaded.id}, total={calculate_total(loaded)}")


if __name__ == "__main__":
    main()
