# Realization / Implementation (Implements)

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class GCash(Payment):
    def pay(self, amount):
        print("Paid", amount, "using GCash")

# Run
payment = GCash()
payment.pay(250)
