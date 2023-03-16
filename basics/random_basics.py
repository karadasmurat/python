import random
import time

def main():
    
    # Randomness
    # The random module actually produces pseudorandom (that is, deterministic) numbers 
    # based on an internal state that you can set with random.seed if you want to get reproducible results
    SEED = int(time.time())     # the current time in seconds since the Epoch.
    # SEED = 123
    random.seed(SEED)           # this ensures we get the same results every time
    # test_seed = int(input("Create a seed number: "))

    # always the same numbers! with the same seed
    for i in range(5):
        # num = int(random.random() * 6) # int ( 0 - 5.9999 )
        dice = random.randint(1, 6)
        print(f"roll {i}: {dice}")


    # if you need to randomly choose a sample of elements without replacement (i.e., with no duplicates), you can use random.sample:
    lottery_numbers = range(60)
    winning_numbers = random.sample(lottery_numbers, 6)  
    print(f"winning numbers {SEED=} {winning_numbers=}")   # _seed=123 winning_numbers=[6, 53, 57, 55, 2, 24]

    # To choose a sample of elements with replacement (i.e., allowing duplicates), you can just make multiple calls to random.choice:
    four_with_replacement = [random.choice(range(10)) for _ in range(4)]
    print(f"{SEED=} {four_with_replacement=}")             # _seed=123 four_with_replacement=[8, 8, 5, 5]

    coin_toss()
    roll_dice()
    roll_dice(2)
    # banker_roulette()

    # Return a random element from the non-empty sequence
    fruits = ["banana", "apple", "strawberry", "grapes"]
    fruit = random.choice(fruits)
    print(fruit)


def coin_toss():
    # generate a random number, either 0 or 1. Then use that number to print out Heads or Tails. 
    # 1 means Heads 0 means Tails
    # x = 'Heads' if random.randint(0,1) == 0 else 'Tails'
    x = random.choice(['Heads', 'Tails'])
    print(x)


def roll_dice(face_count = 6):
    # generate a random number, for the interval 1 to faces (inclusive)
    x = random.choice(range(1, face_count+1))
    print(x)



# Ask for the names of the table. Select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
def banker_roulette():
    names = []
    while True:
        user_input = input("Enter a name or [Q]uit: ")
        if user_input.lower() in ["q", "quit"]:
            break
        names.append(user_input)

    if(len(names) != 0):
        print (random.choice(names), "will pay the bill today!")



if __name__ == "__main__":
    main()