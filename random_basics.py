import random

def main():
    # test_seed = int(input("Create a seed number: "))
    test_seed = 1
    random.seed(test_seed)

    # allways the same numbers! - seed = 1
    for i in range(5):
        # num = int(random.random() * 6) # int ( 0 - 5.9999 )
        dice = random.randint(1, 6)
        print(f"roll {i}: {dice}")

    coin_toss()
    banker_roulette()

    # Return a random element from the non-empty sequence
    fruits = ["banana", "apple", "strawberry", "grapes"]
    fruit = random.choice(fruits)
    print(fruit)


def coin_toss():
    # generate a random number, either 0 or 1. Then use that number to print out Heads or Tails. 
    # 1 means Heads 0 means Tails
    x = 'Heads' if random.randint(0,1) == 0 else 'Tails'
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