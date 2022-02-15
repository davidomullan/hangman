#This Python Program runs a game of hangman.

#Load English Dictionary
import json

#Select Random Word
import random

def print_gallow():
    print("   +---+\n",
          "  |   |\n",
          "      |\n",
          "      |\n",
          "      |\n",
          "      |\n",
          "=========''', '''") 

def print_head():
    print("   +---+\n",
          "  |   |\n",
          "  O   |\n",
          "      |\n",
          "      |\n",
          "      |\n",
          "=========''', '''")

def print_torso():
    print("   +---+\n",
          "  |   |\n",
          "  O   |\n",
          "  |   |\n",
          "      |\n",
          "      |\n",
          "=========''', '''")

def print_right_arm():
    print("   +---+\n",
          "  |   |\n",
          "  O   |\n",
          " /|   |\n",
          "      |\n",
          "      |\n",
          "=========''', '''")

def print_left_arm():
    print("   +---+\n",
          "  |   |\n",
          "  O   |\n",
          " /|\  |\n",
          "      |\n",
          "      |\n",
          "=========''', '''")

def print_right_leg():
    print("   +---+\n",
          "  |   |\n",
          "  O   |\n",
          " /|\  |\n",
          " /    |\n",
          "      |\n",
          "=========''', '''")

def print_left_leg():
    print("   +---+\n",
          "  |   |\n",
          "  O   |\n",
          " /|\  |\n",
          " / \  |\n",
          "      |\n",
          "=========''', '''")

def print_scene(wrong_letters):
    if wrong_letters == 0:
        print_gallow()
    elif wrong_letters == 1:
        print_head()
    elif wrong_letters == 2:
        print_torso()
    elif wrong_letters == 3:
        print_right_arm()
    elif wrong_letters == 4:
        print_left_arm()
    elif wrong_letters == 5:
        print_right_leg()
    else:
        print_left_leg()

#Return next guess, return char
def ask_new_letter():
    while True:
        letter = input("Guess a letter: ")
        if letter.isalpha() and len(letter) == 1:
            return letter
        else:
            continue
        
#Check if letter in word, return bool
def check_letter(random_word, letter):
    return letter in random_word

#Check if letter already guessed
def check_guesses(correct_chars, wrong_chars, letter):
    if letter in correct_chars:
        return True
    elif letter in wrong_chars:
        return True
    else:
        return False

def print_current(random_word, correct_chars):
    current = []
    for i in random_word:
        if i in correct_chars:
            current.append(i)
        else:
            current.append(" ")
    print(current)
    return current

##########################################################
    
try:
    f = open("words_dictionary.json")
    data = json.load(f)
except:
    print("Failed to load dictionary.")

random_word = random.choice(list(data))
print(random_word)

correct_chars = []
wrong_chars = []

while len(wrong_chars) < 6:
    print_scene(len(wrong_chars))
    letter = ask_new_letter()
    if check_guesses(correct_chars, wrong_chars, letter):
        print("Letter already guessed!")
        print("\n")
        
    elif check_letter(random_word, letter):
        print("Congrats! Correct Letter!")
        correct_chars.append(letter)
        print("Correct Letters: ", correct_chars)
        current = print_current(random_word, correct_chars)
        print("\n")
        temp_current = ''.join(current)
        if temp_current == random_word:
            print("Congrats! You guessed it!")
            break
        
    else:
        print("That letter is not in the word!")
        wrong_chars.append(letter)
        print("Incorrect Letters: ", wrong_chars)
        current = print_current(random_word, correct_chars)
        print("\n")

print("The word was", random_word)
