from itertools import count
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

    if character_guess == murderer: #selection to assess the accuracy of guesses
        count = count + 1
    if weapon_guess == murder_weapon:
        count = count + 1
    if room_guess == murder_room:
        count = count + 1

    print(count, " guesses correct")
while True:
    get_info()
    for i in range(0,10): #iteration to only give 10 guesses
        assess_guess()
        if count == 3:
            print("fully correct")
            break
        if i == 9: 
            print("you lost")
            print(murderer)
            print(murder_weapon)
            print(murder_room)