# Association (Knows-a)

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        customer.orders.append(self)

# Run
alice = Customer("Alice")
order1 = Order(101, alice)
order2 = Order(102, alice)

print("Customer:", alice.name)
print("Orders:")
for order in alice.orders:
    print("- Order ID:", order.order_id)
