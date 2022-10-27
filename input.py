def main():
    generate_band_name()
    add_digits_of_2_digit_number()

def generate_band_name():
    print("Welcome to the band name generator")

    city = input("What's the name of the city you grew up in? ")
    pet = input("What's your pet's name? ")

    print("Your band name could be", city, pet)


def add_digits_of_2_digit_number():
    two_digit_number = input("Type a two digit number: ")
    print(int(two_digit_number[0]) + int(two_digit_number[1]))


main()