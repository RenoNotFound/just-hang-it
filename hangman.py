import random

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
    # list(word)
    return hashed_cap

# print(get_hashed(pick_capital()))

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
    # if letter in password:
    #     print("Correct", letter)
    for i, x in enumerate(password):
        if x == letter:
            hashed_password[i] = letter
    # else:
    #     print('')
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
    pass


def is_win(hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered

    Args:
    str: The hashed password
    str: The password

    Returns:
    bool:
    '''
    pass


def is_loose(life_points):
    '''
    Checks if life points is equal 0

    Args:
    int: The life life_points

    Returns:
    bool: True if life point is equal 0, False otherwise
    '''
    pass


def get_input():
    '''
    Reads a user input until it contains only letter

    Returns:
    str: The validated input
    '''
    letter = input("Try to guess it!: ").upper()
    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    while letter not in alphabet:
        print("Please use only single letters.")
        letter = input("Try to guess it!: ")
    return letter


def main():

    print("Welcome to Hangman!")
    print("Enter 'start' to start the game")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    cap = pick_capital()
    hashed_cap = get_hashed(cap)
    print("A randomized European city has been selected.")

    while True:
        if user_input == "quit":
            break
        elif user_input == "start":
            print(' '.join([x + ' ' for x in hashed_cap]))
            letter = get_input()
            uncover(hashed_cap, cap, letter)

    print(uncover(hashed_cap, cap, letter))


if __name__ == '__main__':
    main()