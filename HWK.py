class Vehicle:
    def __init__ (self, capacity):
        self.capacity = capacity
    
    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        return base_fare + (0.1 * base_fare)

x=int(input("Enter the capacity of the bus: "))
bus = Bus(x)
print("Total Bus fare is:", bus.fare())