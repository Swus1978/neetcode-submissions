class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        self.hunger -= 1
        # and print a message about feeding the pet
        print('Fluffy has been fed.')
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
for _ in range(3):
    my_pet.feed()
    print(f"{my_pet.name}'s hunger level: {my_pet.hunger}")

