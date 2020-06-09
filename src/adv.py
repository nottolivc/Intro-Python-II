from room import Room
from player import Player
from item import Item

# declare all items and rooms

items = {
    'outside': [],
    'foyer': [Item("Key", " key for something"), Item("Sword", "A Spanish Sword")],
    'overlook': [Item("Knife", "battle knife")],
    'narrow': [Item("Matches", "matches to light fire")],
    'treasure': [Item("Gold", "A chest of gold bars.")],
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items['outside']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items['foyer']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items['overlook']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items['narrow']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Gold bars are littered all over the grounds. You must pick up what you can take, and come back.
The only exit is to the south.""", items['treasure']),
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare player w input
player = Player(input("What is your name? \n"), room['outside'])

# Write a loop that:

while True:
    # Prints the current room name
    print(f"You are at: {player.location} \ninventory: {player.inventory}")
    # Prints the current description (the textwrap module might be useful here).
    # print(player.location.description)
    print()
    # Waits for user input and decides what to do.
    user_input = input(
        "\nEnter a direction (N)orth,(E)ast,(S)outh,(W)est or Q to quit, type GET/DROP Item: ")
    # handle multiple args
    CHOICES = user_input.split(' ')
    # If the user enters a cardinal direction, attempt to move to the room there.
    if(user_input == 'n' or user_input == 'N'):
        target = player.location.n_to
    elif(user_input == 's' or user_input == 'S'):
        target = player.location.s_to
    elif(user_input == 'e' or user_input == 'E'):
        target = player.location.e_to
    elif(user_input == 'w' or user_input == 'W'):
        target = player.location.w_to
    elif len(user_input) > 1:
        if CHOICES[0].upper() == "GET":
            player.get_item(CHOICES[1].upper())
        elif CHOICES[0].upper() == "DROP":
            player.drop_item(CHOICES[1].upper())
        else:
            print("\nInvalid command.")
    # If the user enters "q", quit the game.
    elif(user_input == 'q' or user_input == 'Q'):
        break
    if(target != None):
        player.move(target)
    else:
        print("Invalid direction")

    print('\n')
