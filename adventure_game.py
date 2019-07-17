import time
import random


item = []
options = ['1', '2', 'y', 'n']

monsters = ['Medusa', 'Dragon', 'Mother-in-Law',
            'Troll', 'Mad Knight', 'Barbarian']
random_monster = random.choice(monsters)

weapons = ['Excalibur', 'Lanister Magician Staff',
           'Gold Champion Dagger', 'Meteor Whip of Doom']
random_weapon = random.choice(weapons)


def pr(word):
    time.sleep(1)
    print(word)


def intro():
    pr("You find yourself standing in an open field, filled "
       "with grass and yellow wildflowers.")
    pr("Rumor has it that a " + random_monster + " is somewhere around here, "
       "and has been terrifying the nearby village.")
    pr("In front of you is a house.")
    pr("To your right is a dark cave.")
    pr("In your hand you hold your trusty "
       "but not very effective dagger.")


def valid_input(prompt):
    while True:
        Answer = str(input(prompt))
        if Answer in options:
            return Answer
        pr("Enter the right answer")


def beginning():
    pr("\nEnter 1 to knock on the door of the house.")
    pr("Enter 2 to peer into the cave.\n ")

    response = valid_input("What would you like to do?\n "
                           "(Please enter 1 or 2)\n ")

    if response == '1':
        pr("You approach the door of the house.")
        pr("You are about to knock when the door "
           "opens and out steps a " + random_monster)
        pr("Eep! This is the " + random_monster + "'s house!")
        pr("You feel a bit nervous for this. And... "
           + random_monster + " see you!")

        reaction = valid_input("Would you like to (1) fight or"
                               " (2) run away?\n")

        if random_weapon in item:
            if reaction == '1':
                goodEnding()
            elif reaction == '2':
                pr("You run back into the field. Luckily,"
                   " you don't seem to have been followed.")
                beginning()
        else:
            if reaction == '1':
                earlyDead()
                startAgain()
            elif reaction == '2':
                pr("You run back into the field. Luckily, "
                   "you don't seem to have been followed.")
                beginning()

    elif response == '2':
        if random_weapon in item:
            pr("The cave is empty.")
            pr("You decide to go back to the field")
            beginning()
        else:
            getWeapon()
            beginning()


def earlyDead():
    pr("You do your best...")
    pr("but your dagger is no match for the " + random_monster)
    pr("You have been defeated...")


def getWeapon():
    pr("You peer cautiously into the cave.")
    pr("It turns out to be only a very small cave.")
    pr("Your eye catches a glint of metal behind a rock.")
    pr("You have found the magical weapon, it's the " + random_weapon + " !\n")
    item.append(random_weapon)
    pr("You discard your silly old dagger and take the weapon with you.")
    pr("You walk back out to the field, and have "
       "more confidence to fight the " + random_monster)


def goodEnding():
    pr("Your weapon shines brightly in your hand as you "
       "brace yourself for the attack of" + random_monster)
    pr("But the " + random_monster + " takes one look at "
       "your shiny new toy and runs away!")
    pr("You have rid the dangerous monster. "
       "You are the new Champion!!")
    startAgain()


def startAgain():
    response = valid_input("Would you like to play again? (y/n)")

    if response == 'y':
        pr("Excellent! Restarting the game ...")
        intro()
        beginning()
    elif response == 'n':
        pr("Thank you for playing Adventure Game! See you again.")
        time.sleep(1)
        exit()


def play_game():
    intro()
    beginning()


play_game()
