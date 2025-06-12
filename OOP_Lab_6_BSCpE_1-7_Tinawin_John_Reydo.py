class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    # Getter methods
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed
    
    # Setter methods
    def set_year_model(self, year_model):
        self.__year_model = year_model

    def set_make(self, make):
        self.__make = make

    def set_speed(self, speed):
        self.__speed = speed

    # Accelerate and brake
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5

my_car = Car (2025, "Mitsubishi Montero Sport")

# Accelerate 5 times
print("Accelerating:")
for _ in range(5):
    my_car.accelerate()
    print("Current speed: ", my_car.get_speed())

# Brake 5 times
print("\nBraking:")
for _ in range(5):
    my_car.brake()
    print("Current speed: ", my_car.get_speed())