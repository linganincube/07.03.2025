class Vehicle:
    """Base class for vehicles."""

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        """Generic engine start method."""
        return "Engine starting..."

    def get_vehicle_type(self):
        """Returns a generic vehicle type."""
        return "Generic Vehicle"

    def display_info(self):
        """Displays basic vehicle information."""
        print(f"Make: {self.make}, Model: {self.model}, Type: {self.get_vehicle_type()}")
        print(self.start_engine())


class Car(Vehicle):
    """Subclass representing a car."""

    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def start_engine(self):
        """Overrides the engine start method for cars."""
        return "Car engine starting... Vroom!"

    def get_vehicle_type(self):
        """Overrides the vehicle type for cars."""
        return "Car"

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Bike(Vehicle):
    """Subclass representing a bike."""

    def __init__(self, make, model, num_wheels):
        super().__init__(make, model)
        self.num_wheels = num_wheels

    def start_engine(self):
        """Overrides the engine start method for bikes."""
        return "Bike engine starting... Brum brum!"

    def get_vehicle_type(self):
        """Overrides the vehicle type for bikes."""
        return "Bike"

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")

# Example usage
car = Car("Toyota", "Camry", 4)
bike = Bike("Honda", "CBR", 2)
generic_vehicle = Vehicle("Generic", "Vehicle")

print("Car:")
car.display_info()
print("\nBike:")
bike.display_info()
print("\nGeneric Vehicle:")
generic_vehicle.display_info()