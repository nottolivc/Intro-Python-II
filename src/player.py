from room import Room


class Player:
    def __init__(self, name, location):
        self.name = name
        #self.items = items
        self.location = location
        self.inventory = []

    def __str__(self):
        return f'{self.name} is in {self.location} with {self.items}.'

    def move(self, new_room):
        print(f'\n{self.name} has switched rooms to {self.location}.')
        self.location = new_room

    def get_item(self, item):
        for x in self.location.items:

            if x.name.upper() == item:
                self.location.remove_item(x)
                self.inventory.append(x)
                print(f'\n{self.name} has grabbed the {x.name}')

            else:
                print("Not available in this room.")

    def drop_item(self, item):
        for x in self.inventory:

            if x.name.upper() == item:
                self.inventory.remove(x)
                self.location.add_item(x)
                print(f'\n{self.name} has dropped the {x.name}')

            else:
                print("Doesn't exist.")
