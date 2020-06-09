from room import Room


class Player:
    def __init__(self, name, location):
        self.name = name
        #self.items = items
        self.location = location
        self.inventory = []

    def __str__(self):
        return f'{self.name} is in {self.location} with {self.inventory}.'

    def move(self, new_room):
        # self.new_room = new_room
        self.location = new_room
        print(f'\n{self.name} has switched rooms from {self.location}.')

    def get_item(self, item):
        # self.location.remove_item(item)
        self.inventory.append(item)
        print(f'\n{self.name} has grabbed the {x.name}')

    def drop_item(self, item):
        self.inventory.remove(item)
        # self.location.add_item(item)
        print(f'\n{self.name} has dropped {x.name}')
