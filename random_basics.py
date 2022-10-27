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

    # Return a random element from the non-empty sequence
    fruit = random.choice(["banana", "apple", "orange", "strawberry", "grapes"])
    print(fruit)


def coin_toss():
    # generate a random number, either 0 or 1. Then use that number to print out Heads or Tails. 
    # 1 means Heads 0 means Tails
    x = 'Heads' if random.randint(0,1) == 0 else 'Tails'
    print(x)




if __name__ == "__main__":
    main()