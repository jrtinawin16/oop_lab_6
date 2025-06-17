from myPet import Pet
name = input("Enter your pet's name: ")
animal_type = input("Enter type of animal (Dog, Bird, Fish): ")
age = input("Enter your pet's age: ")

my_pet = Pet()
my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(age)