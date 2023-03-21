import os
from typing import List
from domain import MenuItem

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def introduce():
    print("utils> hello, world.")

# one-liner for boolean return type
def is_positive(x):
    return x > 0        # boolean - if parantez icini direkt return edebilirsin

# one-liner for boolean return type
def is_even(x):
    return x % 2 == 0   # boolean

def printTitle(title):
    print(f"\n{title}")
    print("-" * len(title))


def show_menu(header: str, menuItems: List[MenuItem]):
    clear_terminal()
    print("\n" + header + "\n")

    for index, value in enumerate(menuItems):
        print(f"[{index+1}] {value.text}")      # use .text attribute for the labels printed.

    try:
        selected = int(input("\nEnter your choice: "))
        if selected < 1 or selected > len(menuItems):
            print("Invalid choice.")
            raise ValueError("Only integers in the menu are allowed.")

    except ValueError:
        print("Invalid choice.")
        raise ValueError("Only integers are allowed.")

    return menuItems[selected-1].value      # return .value attribute, the wrapped object.

