import random
import os
import csv
from typing import List

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

categories = ['İsim', 'Eşya', 'Hayvan']
# selected_category = categories[2]
MASK = '🟦'
MAX_LIVES = 6


def setup_new_game():
    lives = MAX_LIVES
    guesses = []


def main():

    win = False
    lives = MAX_LIVES
    # guesses = set()    # set
    guesses = []
    rounds_win = 0
    rounds = 0

    # Clear the Screen
    clear_screen()

    print(HEADER)
    # player = login()
    # print(f"Welcome, {player}")

    gameover = False
    while not gameover:
        rounds += 1

        # Clear the Screen
        # clear_screen()    # this would clear game title as well.

        # print("GET READY FOR A NEW ROUND!")

        # TODO oynanan kelime tekrar etmesin.
        selected_category = selectAnOption("Kategoriler:", categories)
        # print(f"{selected_category=}")

        secret = get_secret_word(selected_category)
        # print("? =", secret)
        masked_secret = mask_word(secret)
        # print("Kategori:", selected_category)
        print(format_masked_list(masked_secret))

        while True:
            # game loop for each round

            (endOfRound, win) = the_end(masked_secret, lives)
            if endOfRound:
                if win:
                    rounds_win += 1
                else:
                    print(f"The secret word: {secret}")

                # The end of this round. Ask for another.
                play_again = selectAnOption("Play Again?:", ["Yes", "No"])
                if play_again == "No":
                    gameover = True
                else:
                    # setup_new_game()
                    lives = MAX_LIVES
                    guesses = []

                # exit this round.
                break

            guess = input("\nPick a letter: ").upper()

            # Clear the Screen
            clear_screen()

            # guesses.add(guess)    # add to set
            guesses.append(guess)   # append to list
            # guess = 'G'
            is_good_guess = check(guess, secret, masked_secret)
            if not is_good_guess:
                lives -= 1

            print("Kategori:", selected_category, "\n")
            print(format_masked_list(masked_secret), "\t\t", health_info(lives, guesses))
            # break

    # print_score(win, secret)
    print_score_rounds(rounds_win, rounds)


def print_score_rounds(rounds_win, rounds):
    # print("GAME OVER.")
    # print("You won", score, "rounds.")

    scoreboard = f"""
￣￣￣￣￣￣￣￣￣￣￣￣
    GAME OVER.
    Score: {rounds_win} / {rounds}
                      
￣￣￣￣￣￣￣￣￣￣￣￣
     (\__/)  ||
     (•ㅅ•)  ||
     /  　  づ
"""

    print(scoreboard)


def print_score(win, secret):
    win_desc = f"🌟 Yaay !"
    loose_desc = f"Game Over.\nThe secret word: {secret}\n"

    scoreboard = f"""
￣￣￣￣￣￣￣￣￣￣￣￣
    
    {win_desc if win else loose_desc}
                      
￣￣￣￣￣￣￣￣￣￣￣￣
     (\__/)  ||
     (•ㅅ•)  ||
     /  　  づ
"""

    print(scoreboard)


def selectAnOption(prompt, options):
    # surround first char of option with [ ]
    # print(f"{options=}")
    ops = ""
    for option in options:
        option = ' [' + option[0].upper() + ']' + option[1:]    # [Y]es
        ops += option + "\n"
    print("\n", prompt)
    print(ops)
    # choice = input(f"{prompt} {ops}: ").upper()
    choice = input(f"Seçiminiz > ").upper()
    # print(f"{choice=}")
    for option in options:
        # print(f"{option=}")
        if choice == option[0].upper() or choice == option:
            return option


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
        return (True, False)     # (end=True, win=False)
    elif MASK not in the_list:
        return (True, True)     # (end=True, win=True)

    return (False, None)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        # str = f"{str} {i} "
        str += " " + i
    return str


def health_info(lives, guesses):
    return (f"{'🟢' * lives}{'🔴' * (MAX_LIVES-lives)} {guesses}")   #


def get_secret_word(category=None):

    all_words = getwords_csv("data/words.csv")
    # print(f"{all_words=}")
    words_of_category = []
    if category:
        for w in all_words:
            if w['category'] == category:
                words_of_category.append(w)
    else:
        words_of_category = all_words

    return random.choice(words_of_category)['word']


def getwords_csv(fname: str, delimiter=',') -> List[dict]:

    print(f"Reading from csv file: {fname} ...")

    words = []
    with open(fname) as file:
        reader = csv.DictReader(file, delimiter=delimiter)   # when we iterate over reader, each row will be of type dict.
        for row in reader:
            # print("row:", row)
            words.append(row)   # {'category': 'Hayvan', 'word': 'RAKUN'}

    return words


if __name__ == "__main__":
    main()
