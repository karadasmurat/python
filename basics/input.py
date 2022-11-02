# import colors
RED = "\033[31m"
ENDC = '\033[0m'

def main():
    # generate_band_name()
    # add_digits_of_2_digit_number()
    
    avg = avg_scores()
    print(f"{avg=}")

def generate_band_name():
    print("Welcome to the band name generator")

    city = input("What's the name of the city you grew up in? ")
    pet = input("What's your pet's name? ")

    print("Your band name could be", city, pet)


def add_digits_of_2_digit_number():
    two_digit_number = input("Type a two digit number: ")
    print(int(two_digit_number[0]) + int(two_digit_number[1]))

def avg_scores():
    scores = input("Input list of scores, seperated by a space (i.e. 75 60 95): ").split()
    if len(scores) == 0:
        return 0.0

    sum = 0;
    try:
        for score in scores:
            sum += int(score)
    except ValueError:
        print(f"{RED}Scores should be seperated by a space, i.e. 75 60 95{ENDC}")
        return 0.0
    
    return round(sum / len(scores), 2)


main()