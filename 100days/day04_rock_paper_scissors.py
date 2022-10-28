import random

def main():
    options = ["Rock", "Paper", "Scissors"]
    # input 0 rock, 1 paper, 2 scissors
    usr = get_input("What do you choose?", options).lower()



    # make a random choice for the computer
    comp = random.choice(['r', 'p', 's'])
    print("Computer:", comp)

    # apply the rules to select the winner
    check_first_wins(usr, comp)

    # if usr.lower() in ['r', "rock"]:
    #     if(comp == "Rock"):
    #         print("No winner.")
    #     elif comp == "Paper":
    #         print("💀 You loose.")
    #     else:
    #         print("🎉 🥳 You win")

    # if usr.lower() in ['p', "paper"]:
    #     if(comp == "Paper"):
    #         print("No winner.")
    #     elif comp == "Scissors":
    #         print("💀 You loose.")
    #     else:
    #         print("🎉 🥳 You win")

    # if usr.lower() in ['s', "scissors"]:
    #     if(comp == "Scissors"):
    #         print("No winner.")
    #     elif comp == "Rock":
    #         print("💀 You loose.")
    #     else:
    #         print("🎉 🥳 You win")

    # inform player

def check_first_wins(p1, p2):
    wins = {"r": "s", "p":"r", "s":"p"}
    if p1 == p2:
        print("No winner.")
        return 'draw'
    elif wins[p1] == p2:
        print("🎉 🥳 You win")
        return 'win'
    else:
        print("💀 You loose.")
        return 'loose'


def get_input(question, options):
    # surround first char of option with [ ]
    ops = "\nSelect:"
    for option in options:
        option = ' [' + option[:1] + ']' + option[1:]
        ops += option
    
    return input(f"{question} {ops}: ")


if __name__ == "__main__":
    main()