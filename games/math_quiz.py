# Objective of Game
# Provide the right answer for the question.

# The game comes to an end after a fixed number of lives.
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


def main():
    LIVES = 3
    question_num = 1
    score = 0

    player = login()
    print(f"Welcome, {player}")

    last_score = find_score_by_player(player)
    if last_score != -1:
        print(f"High Score: 🏆 {last_score}\n")

    while (LIVES > 0):
        # q_json = {"q": "4*2"}
        question = get_question()
        
        user_answer = int(input(f"{question_num}) {question['q']} = "))
        question_num += 1
        try:
            assert question['a'] == user_answer
            score += 1
            lives_info(LIVES, 3)
        except AssertionError:
            LIVES -= 1
            lives_info(LIVES, 3)

    

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

def lives_info(have, max):
    print("\t\t\t", end="")
    for i in range(max - have):
        print("🔴 ", end="")
    for i in range(have):
        print("🟢 ", end="")
    
    print() # new line

def print_score(is_highest, score):
    regular = f"🌟 {score}"
    record = f"{regular}\n\t🏆 New highest score!"

    GAME_OVER = f"""
*********************************
\tGame Over.
\t{record if is_highest else regular}
*********************************
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

    op1 = random.randint(2, 9)
    op2 = random.randint(2, 9)
    operation = random.choice(["+", "*"])

    q_str = f"{op1} {operation} {op2}"
    answer = eval(q_str)
    q_json = {"q": q_str, "a":answer}

    #print(f"{num}) {q_str}")
    return q_json


if __name__ == "__main__":
    main()
