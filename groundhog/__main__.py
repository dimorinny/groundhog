import time

from .character import Character

def cast_around(character: Character):
    for _ in range(10):
        character.target()
        character.cast('3')
        character.target()
        character.cast('3')
        character.target()
        character.cast('3')
        character.target()
        character.cast('3')
        character.turn(45)

def loop(character: Character):
    while True:
        cast_around(character=character)
        character.move(8)

# TODO: detect game is opened to start playing
time.sleep(2)

character = Character()
loop(character=character)
