class Order:
    def __init__(self, customer, coffee, price):
        if not (isinstance(price, float) or isinstance(price, int)):
            raise TypeError("Price must be a number.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
