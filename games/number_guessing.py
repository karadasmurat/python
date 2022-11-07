import random

RED = "\033[31m"
GREEN = "\033[32m"
ENDC = '\033[0m'

def main():
    print("Welcome.")
    secret = random.randint(1, 100)

    for _round in range(7):
        guess = int(input("Make a guess [1-100]: "))
        if guess == secret:
            print("🌟 You win!")
            break
        elif guess > secret:
            print(f"{live_info(_round, 7)} Nope. Try a smaller guess.")
        else:
            print(f"{live_info(_round, 7)} Nope. Try a larger guess.")

    print(f"Game over. How about {secret}?")
        

def live_info(round, lives):
    return (f"{GREEN + '♥️' * (lives - (round+1)) + RED + '♥️' * (round+1) + ENDC}")

if __name__ == "__main__":
    main()