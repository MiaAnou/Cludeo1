import random
characters = ("Professor Plum", "Mrs White","Mr Green", "Mrs Peacock", "Miss Scarlett", "Colonel Mustard")
weapons = ("wrench", "candlestick","lead pipe", "rope", "revolver", "knife")
rooms = ("Study", "Kitchen","Hall", "Conservatory", "Lounge", "Ballroom", "Dining Room", "Libary", "Billiard Room")

murderer = characters[random.randint(0,5)]
murder_room = rooms[random.randint(0,5)]
murder_weapon = weapons[random.randint(0,5)]

