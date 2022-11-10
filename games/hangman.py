import random
import os
import csv

HEADER = """
██╗░░██╗███████╗██╗░░░░░██╗███╗░░░███╗███████╗
██║░██╔╝██╔════╝██║░░░░░  ║████╗░████║██╔════╝
█████═╝░█████╗░░██║░░░░░██║██╔████╔██║█████╗░░
██╔═██╗░██╔══╝░░██║░░░░░██║██║╚██╔╝██║██╔══╝░░
██║░╚██╗███████╗███████╗██║██║░╚═╝░██║███████╗
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝╚═╝░░░░░╚═╝╚══════╝

██████╗░░█████╗░██████╗░████████╗██╗░██████╗██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ║██╔════╝  ║
██████╔╝███████║██████╔╝░░░██║░░░██║╚█████╗░██║
██╔═══╝░██╔══██║██╔══██╗░░░██║░░░██║░╚═══██╗██║
██║░░░░░██║░░██║██║░░██║░░░██║░░░██║██████╔╝██║
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░╚═╝

"""

categories = ['Isim', 'Esya', 'Hayvan']
selected_category = categories[2]
MASK = '-'

def main():

    win = False
    lives = 3
    # guesses = set()    # set
    guesses = []

    # Clear the Screen
    clear_screen()

    print(HEADER)
    # player = login()
    # print(f"Welcome, {player}")

    # TODO oynanan kelime tekrar etmesin.
    secret = get_secret_word(selected_category)
    print("? =", secret)
    masked_secret = mask_word(secret)
    print(format_masked_list(masked_secret))

    while True:
        (end, win) = the_end(masked_secret, lives)
        if end:
            break
        
        guess = input("\nPick a letter: ").upper()

        # Clear the Screen
        clear_screen()

        # guesses.add(guess)    # add to set
        guesses.append(guess)   # append to list
        #guess = 'G'
        is_good_guess = check(guess, secret, masked_secret)
        if not is_good_guess:
            lives -= 1

        print(format_masked_list(masked_secret), "\t\t",health_info(lives, guesses))
        # break
    
    if win:
        print("Yaay !")
    else:
        print("Game Over.")


# List passed by reference ?
def check(letter, word, the_list):
    '''Return True if letter is in word.'''
    found = False
    for i in range(len(word)):
        if word[i] == letter:
            the_list[i] = letter
            found = True
    return found
    

def the_end(the_list, lives):
    if lives < 1:
        return(True, False)     # (end=True, win=False)
    elif MASK not in the_list:
        return (True, True)     # (end=True, win=True)

    return (False, None)


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def login():
    return input("Nick? ")

def mask_word(word):
    masked = []
    for letter in word:
        masked.append(MASK)
    
    return masked

def format_masked_list(masked_list):
    str = "\n"
    for i in masked_list:
        str = f"{str} {i} "
    return str

def health_info(lives, guesses):
    return (f"{'🟢' * lives} {guesses}")   # 🔴

def get_secret_word(category=None):

    all_words = read_csv("data/words.csv")
    sub_list = []
    if category:
        for entry in all_words:
            if entry['category'] == category:
                sub_list.append(entry)
    else:
        sub_list = all_words

    return random.choice(sub_list)['word']

def read_csv(fname, delimiter=','):

    print(f"Reading from csv file: {fname} ...")

    words = []
    with open(fname) as file:
        reader = csv.DictReader(file, delimiter=delimiter)   # when we iterate over reader, each row will be of type dict.
        for row in reader: 
            words.append(row)

    return words

if __name__ == "__main__":
    main()