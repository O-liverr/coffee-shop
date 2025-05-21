from customer import Customer
from coffee import Coffee
from order import Order

jane = Customer("Jane")
john = Customer("John")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

jane.create_order(latte, 3.5)
jane.create_order(mocha, 4.0)
john.create_order(latte, 5.0)

print(f"{jane.name} ordered: {[c.name for c in jane.coffees()]}")
print(f"Latte was ordered by: {[c.name for c in latte.customers()]}")
print(f"Average price for Latte: {latte.average_price():.2f}")
print(f"Most aficionado for Latte: {Customer.most_aficionado(latte).name}")
