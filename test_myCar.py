from myCar import Car
my_car = Car(2025, "Mitsubishi Montero Sport")

# Accelerate 5 times
print("Accelerating:")
for i in range(5):
    my_car.accelerate()
    print(f"Your car {my_car.get_make()}{my_car.get_year_model()}'s current speed: ", my_car.get_speed())

# Brake 5 times
print("\nBraking:")
for i in range(5):
    my_car.brake()
    print("Current speed: ", my_car.get_speed())    