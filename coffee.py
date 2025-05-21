class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

if __name__ == "__main__":
    from customer import Customer
    from order import Order

    coffee = Coffee("Cappuccino")
    customer = Customer("Brian")

    customer.create_order(coffee, 3.0)
    customer.create_order(coffee, 4.0)

    print(f"Coffee name: {coffee.name}")
    print(f"Number of orders: {coffee.num_orders()}")
    print(f"Customers who ordered: {[cust.name for cust in coffee.customers()]}")
    print(f"Average price: {coffee.average_price():.2f}")
