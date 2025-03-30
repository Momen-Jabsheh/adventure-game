import time
import random


def print_sleep(promt, s_time):
    print(promt)
    time.sleep(s_time)


def intro():
    print_sleep("welcome", 1)
    print_sleep("You find yourself standing in an open field "
                " filled with grass and yellow wildflowers.", 2)


def choise_system(first_choise, second_choise, message):
    print_sleep(message, 2)
    print_sleep("you have two choises :", 1)
    print_sleep("1." + first_choise + "\n" + "2." + second_choise, 2)
    while True:
        decision = input("choise [1 or 2] \n")
        if (not decision.isdigit()):
            print_sleep("please use numbers ", 2)
        elif (int(decision) != 1 and int(decision) != 2):
            print_sleep("i do not understand", 1)
            print_sleep("try again", 0.5)
        else:
            return int(decision)


def win():
    win_word = ["congratulations ! \nyou won ", "you won by a miracle"]
    print_sleep(random.choice(win_word), 2)


def lost():
    lose_word = ["Better luck next time!",
                 "you lost this round.", "game over"]
    print_sleep(random.choice(lose_word), 2)


def random_math_q():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.choice(['+', '-', '*'])
    a = int(input(f"{x} {z} {y} = "))
    if (z == '+' and x + y == a):
        win()
    elif (z == '-' and x - y == a) or (z == '*' and x * y == a):
        win()
    else:
        lost()


def third_descision_aa():
    x = "you are now in a fight"
    a = choise_system("kill the monster", "hurt the monster", x)
    if a == 1:
        win()
    if a == 2:
        y = "if you don't answer this question correctly you will lose"
        print_sleep(y, 2)
        random_math_q()


def secound_descision_a():
    x = "after running for a while you find a sword"
    a = choise_system("take it", "leave it", x)
    if a == 1:
        third_descision_aa()
    if a == 2:
        print_sleep("the monster is so powerful", 1)
        print_sleep("but you can beat him by using the power of math", 2)
        random_math_q()


def third_descision_bb():
    x = "you discoverd how to fly with the boat"
    a = choise_system("fly", "find another solution", x)
    if a == 1:
        win()
    elif a == 2:
        x = random.choice(["sword", "axe", "wand"])
        print_sleep("you found a " + x, 1)
        z = "choise what do you want to do with it"
        y = choise_system("use it", "throw it", z)
        if y == 1:
            win()
        else:
            lost()


def secound_descision_b():
    print_sleep("you jumped on the magic boat", 2)
    x = random.choice(["rock", "tree trunk", "shark", "whale"])
    a = choise_system("skip it", "crash !!", "a " + x + " suddenly appeared")
    if a == 1:
        third_descision_bb()
    if a == 2:
        print_sleep("it turned out the boat wasn't strong enough", 2)
        lost()


def first_descision():
    x = "there is a monster chasing you"
    a = choise_system("Enter the cave", "Enter the river", x)
    if a == 1:
        secound_descision_a()
    elif a == 2:
        secound_descision_b()
    a = choise_system("yes", "no", "do you want to play again")
    if a == 1:
        first_descision()
    else:
        print_sleep("i hope you enjoy playing this game", 2)


intro()
first_descision()
