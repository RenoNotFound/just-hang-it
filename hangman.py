import random
import os

def pick_capital():
    '''
    Picks a random European capital

    Returns:
    str: The name of European capital
    '''
    file_path = 'cities.txt'
    textfile = open(file_path)
    lines = textfile.read().splitlines()
    return random.choice(lines)


def get_hashed(word):

    '''
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.

    Args:
    str: The word to hash

    Returns:
    str: The hashed password
    '''
    hashed_cap = ['_'] * len(word)
    return hashed_cap

def uncover(hashed_password, password, letter):
    '''
    Uncovers all occurences of the given letter in the hashed password based on the password

    Args:
    str: The hashed password
    str: The password
    str: The letter to uncover

    Returns:
    str: The hashed password with uncovered letter
    '''
    for i, x in enumerate(password):
        if x == letter:
            hashed_password[i] = letter
    return hashed_password


def update(used_letters, letter):
    '''
    Appends the letter to used_letters if it doesn't occur

    Args:
    list: The list of already used letters
    str: The letter to append

    Returns:
    list: The updated list of already used letters
    '''

    used_letters.append(letter)
    return used_letters



def is_win(hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered

    Args:
    str: The hashed password
    str: The password

    Returns:
    bool:
    '''
    if hashed_password == password:
        return password


def is_loose(life_points):
    '''
    Checks if life points is equal 0

    Args:
    int: The life life_points

    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    if life_points == 0:
        print("_________")
        print("|	|")
        print("|	O")
        print("|      \|/")
        print("|R.I.P. |")
        print("|      / \ ")
        print("|________")
        print("Oops, looks like you just died! Sad story :(")
    else:
        return life_points


def get_input():
    '''
    Reads a user input until it contains only letter

    Returns:
    str: The validated input
    '''
    letter = input("Try to guess it!: ").upper()
    while letter.isnumeric():
        print("Please use only letters.")
        letter = input("Try to guess it!: ")
    return letter


def starting_screen():
    print("Welcome to Hangman!")
    print("A randomized European city will be selected for you to guess.")
    print("Enter 'start' to start the game")
    print("Enter 'quit' to end the program")

def hangman_wins():
        print("_________")
        print("|	|")
        print("|	    ")
        print("|              O         Thank you clever hooman! ")
        print("|             \|/   ")
        print("|              |")
        print("|________     / \ ")

def hangman_hangs(lifepoint):

    if lifepoint == 6:
        print("_________")
        print("|	|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    if lifepoint == 5:
        print("_________")
        print("|	|")
        print("|	O    what's happening? ")
        print("|")
        print("|")
        print("|")
        print("|________")
    if lifepoint == 4:
        print("_________")
        print("|	|")
        print("|	O    oh snap ")
        print("|       |")
        print("|       |")
        print("|")
        print("|________")
    if lifepoint == 3:
        print("_________")
        print("|	|")
        print("|	O    stop it pls ")
        print("|      \|")
        print("|       |")
        print("|")
        print("|________")
    if lifepoint == 2:
        print("_________")
        print("|	|")
        print("|	O    stop torturing me!!!! ")
        print("|      \|/")
        print("|       |")
        print("|")
        print("|________")
    if lifepoint == 1:
        print("_________")
        print("|	|")
        print("|	O    can't breathe lol ")
        print("|      \|/")
        print("|       |")
        print("|      / ")
        print("|________")
        
        
def main():

    starting_screen()
    user_input = input(": ")
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    cap = pick_capital()
    hashed_cap = get_hashed(cap)
    used_letters = []
    life = 6
    guessed = False

    while life > 0 and guessed == False:
        if user_input == "quit":
            break
        elif user_input == "start":
            hangman_hangs(life)
            print(f'You have {life} tries left')
            print(' '.join([x + ' ' for x in hashed_cap]))
            letter = get_input()
            uncover(hashed_cap, cap, letter)
            if len(letter) == 1:
                if letter not in alphabet:
                    print('Please use only letters.')
                elif letter in used_letters:
                    print('You have already guessed that letter')
                elif (str(hashed_cap).strip("[]").replace("'", "").replace(",", "").replace(" ","") == str(cap)):
                    is_win(hashed_cap, cap)
                    print(str(hashed_cap).strip("[]").replace("'", "").replace(",", " "))
                    print("You won!")
                    hangman_wins()
                    break
                elif letter not in cap:
                    update(used_letters, letter)
                    print('Wrong guess!')
                    print("Used letters: " + str(used_letters).strip("[]").replace("'", ""))
                    life -= 1
                    is_loose(life)
                else:
                    print('You are doing great. Keep guessing!')
            elif len(letter) == len(cap):
                if letter == cap:
                    print("  ".join(cap))
                    print('Well done, you have guessed the word!')
                    hangman_wins()
                    guessed = True
                else:
                    print('Sorry, you guessed the wrong word! :(')
                    life -= 1
                    is_loose(life)

            else:
                print('Wrong guess!')
                life -= 1
                is_loose(life)
        else:
            print('Invalid input!')
            starting_screen()
            user_input = input(": ")

if __name__ == '__main__':
    main()
