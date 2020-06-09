from room import Room


class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        #self.items = items
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return f'{self.name} is in {self.location} with {self.inventory}'

    def move(self, new_room):
        # self.new_room = new_room
        self.location = new_room
        print(f'\n{self.name} has switched rooms from {self.location.name}')

    def get_item(self, item):
        for x in self.location.items:

            if x.name.upper() == item:
                self.location.remove_item(x)
                self.inventory.append(x)
                print(f'\n{self.name} has grabbed a {x.name}')

            else:
                print("Item not found.")

    def drop_item(self, item):
        for x in self.inventory:

            if x.name.upper() == item:
                self.inventory.remove(x)
                self.location.add_item(x)
                print(f'\n{self.name} dropped the {x.name}')

            else:
                print("Item not in your bag.")
