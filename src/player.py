from room import Room


class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        #
        self.location = location
        self.inventory = inventory

    def __str__(self):
        return f'{self.name} is in {self.location} with {self.inventory}'

    def move(self, new_room):
        # self.new_room = new_room
        self.location = new_room
        print(f'\n{self.name} has switched rooms to {self.location.name}')

    def get_item(self, item):
        for i in self.location.items:

            if i.name.upper() == item:
                self.location.remove_item(i)
                self.inventory.append(i)
                print(f'\n{self.name} has grabbed a {i.name}')

            else:
                print("Item not found.")

    def drop_item(self, item):
        for i in self.inventory:

            if i.name.upper() == item:
                self.inventory.remove(i)
                self.location.add_item(i)
                print(f'\n{self.name} dropped the {i.name}')

            else:
                print("Item not in your bag.")
