class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.orders().append(order)

    @classmethod
    def most_aficionado(cls, coffee):
        best_customer = None
        highest_spent = 0
        for customer in set(order.customer for order in coffee.orders()):
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > highest_spent:
                highest_spent = total_spent
                best_customer = customer
        return best_customer

if __name__ == "__main__":
    from coffee import Coffee

    coffee1 = Coffee("Espresso")
    customer1 = Customer("Alice")
    customer1.create_order(coffee1, 3.5)
    customer1.create_order(coffee1, 4.0)

    print(f"Customer name: {customer1.name}")
    print("Coffees ordered:", [c.name for c in customer1.coffees()])
    print("Orders:")
    for o in customer1.orders():
        print(f"  Coffee: {o.coffee.name}, Price: {o.price}")
