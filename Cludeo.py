import random
characters = ("Professor Plum", "Mrs White","Mr Green", "Mrs Peacock", "Miss Scarlett", "Colonel Mustard")
weapons = ("wrench", "candlestick","lead pipe", "rope", "revolver", "knife")
rooms = ("Study", "Kitchen","Hall", "Conservatory", "Lounge", "Ballroom", "Dining Room", "Libary", "Billiard Room")

def get_info(): #procedure to get info for the game
    murderer = characters[random.randint(0,5)]
    murder_room = rooms[random.randint(0,5)]
    murder_weapon = weapons[random.randint(0,5)]


def assess_guess():
    count = 0
    character_guess = input().lower()
    weapon_guess = input().lower()    
    room_guess = input().lower()

    if character_guess == murderer:
        count = count + 1
    if weapon_guess == murder_weapon:
        count = count + 1
    if room_guess == murder_room:
        count = count + 1

    print(count, " guesses correct")

get_info()
assess_guess()