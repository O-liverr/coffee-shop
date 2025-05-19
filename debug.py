from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 5.0)
c2.create_order(coffee1, 6.0)

print(c1.orders())
print(coffee1.customers())
print(coffee1.num_orders())
print(coffee1.average_price())

print(Customer.most_aficionado(coffee1).name)
