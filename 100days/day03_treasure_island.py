def main():
    print('''
            _  _             _  _
    .       /\\/%\       .   /%\/%\     .
        __.<\\%#//\,_       <%%#/%%\,__  .
    .    <%#/|\\%%%#///\    /^%#%%\///%#\\
        ""/%/""\ \""//|   |/""'/ /\//"//'
    .     L/'`   \ \  `    "   / /  ```
            `      \ \     .   / /       .
    .       .      \ \       / /  .
            .        \ \     / /          .
    .      .    ..:\ \:::/ /:.     .     .
    ______________/ \__;\___/\;_/\________________________________
    YwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw
    ''')

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    #user_input = input("Where do you want to go now? [L]eft or [R]ight? ")
    user_input = get_input("Where do you want to go now?", ["Left", "Right"])
    if(user_input.lower() not in ['l', "left"]):
        print("💀 You fell into a hole. Game Over.")
    else:
        user_input = get_input("What now?", ["Swim", "Wait"])
        if(user_input.lower() not in ['w', "wait"]):
            print("💀 Attacked by trout. Game Over.")
        else:
                user_input = get_input("Which door?", ["Red", "Yellow", "Blue"])
                if(user_input.lower() in ['r', "red"]):
                    print("🔥 Burned by fire. Game Over.")
                elif user_input.lower() in ['b', "blue"]:
                    print("💀 Eaten by beasts. Game Over.")
                elif user_input.lower() in ['y', "yellow"]:
                    print("🎉 You win!")
                else:
                    print("💀 Game Over.")

def get_input(question, options):
    # surround first char of option with [ ]
    ops = ""
    for option in options:
        option = ' [' + option[:1] + ']' + option[1:]
        ops += option
    
    return input(f"{question} {ops}: ")



if __name__ == "__main__":
    main()
