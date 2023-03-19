import math
import random

RED = "\033[31m"
GREEN = "\033[32m"
ENDC = '\033[0m'

UPPER_LIMIT = 100
LIVES = math.ceil(math.log2(UPPER_LIMIT)) # based on divide and conquer, eliminating half at each round, so number of rounds is log2(n)

WIN_MESSAGE = f"""
￣￣￣￣￣￣￣￣￣￣
    🌟 You win!
                      
￣￣￣￣￣￣￣￣￣￣
     (\__/) ||
     (•ㅅ•) ||
     /    づ
"""

def main():
    print("Welcome to the number guessing game!")
    secret = random.randint(1, UPPER_LIMIT)
    winner = False
    wrong_guesses = 0

    for _round in range(LIVES):
        guess = int(input(f"Make a guess [1-{UPPER_LIMIT}]: "))
        if guess == secret:
            print(WIN_MESSAGE)
            winner = True
            break
        elif guess > secret:
            wrong_guesses += 1
            print(f"{live_info(wrong_guesses)} Nope. Try a smaller guess.")
        else:
            wrong_guesses += 1
            print(f"{live_info(wrong_guesses)} Nope. Try a larger guess.")

    if not winner:
        print(f"\n ❌ Game over. How about {secret}?")
        

def live_info(wrong_guesses):
    return (f"{'🟢' * (LIVES - wrong_guesses)}{'🔴'* wrong_guesses}")

    

if __name__ == "__main__":
    main()