class Order:
    def __init__(self, customer, coffee, price):
        if not (isinstance(customer, object) and isinstance(coffee, object)):
            raise TypeError("Customer and Coffee must be valid instances.")

        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

if __name__ == "__main__":
    from customer import Customer
    from coffee import Coffee

    c = Customer("Sammy")
    coffee = Coffee("Latte")
    c.create_order(coffee, 5.0)

    for o in c.orders():
        print(f"Order - Customer: {o.customer.name}, Coffee: {o.coffee.name}, Price: {o.price}")
