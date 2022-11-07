# Objective of Game
# Provide the right answer for the question.
# The player's goal is to score as many points as possible with their limited number of lives.

# Mode: Single Player

# The players will tally their points. The player with the most points, wins the game.
# each question has a different points maybe?

# At the end of each round, the progress of the players is scored.

# ask a simple random math operation, i.e 5 * 9 = ?
## Roll the dice maybe?

# Guess my rule kind of questions ??

# get user answer. If false, decrement

# lose by running out of time ?

# End of Game
# There isn’t a set amount of playtime.
# If playing by yourself, beat your own personal score by trying to get the score as high as possible.

import random
import json
import datetime
import os
from threading import Timer


lives = 3
score = 0
has_timeout = False
HEADER = """
█▀▄▀█ ▄▀█ ▀█▀ █░█
█░▀░█ █▀█ ░█░ █▀█

█▀▀ █░█ ▄▀█ █░░ █░░ ▄▀█ █▄░█ █▀▀ █▀▀
█▄▄ █▀█ █▀█ █▄▄ █▄▄ █▀█ █░▀█ █▄█ ██▄

"""


def main():

    #lives = LIVES
    global lives, score
    question_num = 1
    

    # Clear the Screen
    clear_screen()

    print(HEADER)
    player = login()
    print(f"Welcome, {player}")

    last_score = find_score_by_player(player)
    if last_score != -1:
        print(f"🏆 High Score: {last_score}\n")

    while (lives > 0):
        new_round(question_num)

    
    results = {
        "player": player,
        "score": score,
        "date": datetime.datetime.now().strftime("%x")
    }

    is_highest = False
    if not last_score or score > last_score:
        is_highest = True
        update_score(player, results, last_score)

    print_score(is_highest, score)


def new_round(question_num):

    global lives, score, has_timeout
    has_timeout = False
    
    # q_json = {"q": "4*2"}
    question = get_question()
    user_answer = -999

    # Timer class represents an action that should be run only after a certain amount of time has passed.
    timeout = 10
    t = Timer(timeout, time_out)
    t.start()

    try:
        user_answer = int(input(f"{question_num}) {question['q']} = "))
    except ValueError:
        print("?")

    t.cancel()
    question_num += 1
    try:
        assert question['a'] == user_answer
        score += 1 if not has_timeout else 0
    except AssertionError:
        lives -= 1 if not has_timeout else 0
    
    lives_info(lives, 3)

def time_out():
    global lives, has_timeout
    print("Timeout.")
    has_timeout = True
    lives -= 1

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def lives_info(have, max):
    print("\t\t\t", end="")
    for i in range(max - have):
        print("🔴", end="")
    for i in range(have):
        print("🟢", end="")
    
    print() # new line



def print_score(is_highest, score):
    regular = f"🌟 {score}"
    record = f"{regular}\n    🏆 New highe score!"

    GAME_OVER = f"""
￣￣￣￣￣￣￣￣￣￣￣￣
    Game Over.
    {record if is_highest else regular}
                      
￣￣￣￣￣￣￣￣￣￣￣￣
     (\__/)  ||
     (•ㅅ•)  ||
     /  　  づ
"""

    print(GAME_OVER)



def init_file():
    save_score({"scores":[]})

def save_score(data):
    with open("scores.json", "w") as file:
        json.dump(data, file)


def update_score(playername, new_score, old_score):

    with open("scores.json") as file:
        data = json.load(file)
        scores = data['scores']
        if(old_score == -1):
            # no previous score
            # print("No previous score found. Saving...")
            data['scores'].append(new_score)
        else:
            
            previous = {}
            for score in scores:
                if score['player'] == playername:
                    previous = score
                    break
            if previous:
                # print("found previous score", score)
                scores.remove(previous)

            data['scores'].append(new_score)
        
        save_score(data)


def load_scores():
    try:
        with open("scores.json") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Could not find file.")
        init_file()
        # exit(0)
        # return {}
        raise FileNotFoundError
        

def find_score_by_player(playername):
    
    tries = 3
    for i in range(tries):
        try:
            data = load_scores()
        except:
            print("Error, retry:", i)

    #try:
    scores = data['scores']
    for score in scores:
        if score['player'] == playername:
            return score['score']
    #except KeyError:
    #    return -1

    return -1


def login():
    return input("Nick? ")


def get_question():

    op1 = 1
    op2 = 1
    operation = random.choice(["+", "-", "*"])
    if "-" == operation:
        op1 = random.randint(10, 19)
    else:
        op1 = random.randint(2, 9)

    op2 = random.randint(2, 9)


    q_str = f"{op1} {operation} {op2}"
    answer = eval(q_str)
    q_json = {"q": q_str, "a":answer}

    #print(f"{num}) {q_str}")
    return q_json


if __name__ == "__main__":
    main()
