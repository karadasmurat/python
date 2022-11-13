import random
import csv

all_words = []
new_words=[]
categories = ("Eşya", "Hayvan", "İsim", "Şehir")
MAX_LIVES = 3

def main():
    # list of all the inputs from the player
    history = []

    lives = MAX_LIVES
    score = 0

    first_word = get_a_word()['word']
    print("===========================================")
    print(f"Başlangıç kelimesi: {first_word}")
    print("===========================================")

    magic_letter = first_word[-1]
    while lives>0:
        # ask the user for a new word, in a random category
        category = random.choice(categories)
        guess = input(f"{magic_letter} harfi ile başlayan {category}> ")
        
        if guess in history:
            print("Daha önce söylendi.")
            continue
        else:
            # print(guess)
            if(is_correct(key=magic_letter, word=guess, category=category)):
                score += 1
                history.append(guess)
                magic_letter = guess[-1].upper()
                print("🌟\t\t\t\t", health_info(lives, score))
            else:
                lives -= 1
                print("Cevap hatalı gibi gözüküyor.\t", health_info(lives, score))
        
        print("===========================================")

    # end of game
    print_score(score)

    if new_words:
        print("Learned new words, saving ...")
        write_to_file("data/words.csv", new_words)
                


def is_correct(word, key, category):

    global new_words

    # Rule: the "word" starts with the letter "key"
    if word[0].upper() != key.upper():
        return False

    # Rule 2: the word belongs to the "category"
    # print("Checking category ...")
    # 2.1 Check csv
    for data in all_words:
        if data['category'] == category:
            # print("Found an entry:",data['category'],data['word'] )
            if data['word'].upper() == word.upper():
                return True

    # 2.2 if not in csv, ask for confirmation, and append if confirmed.
    confirmation = input(f"\n\t{word.upper()} not found in the main repository. \n\tPlease confirm that the answer is true, in order to save it. \n\t[T]rue [F]alse :")
    if confirmation.upper() in ["T", "TRUE"]:
        # TODO append csv
        new_words.append({'category':category, 'word':word.upper()})
        return True
    return False


def health_info(lives, score):
    return (f"{'🟢' * lives}{'🔴' * (MAX_LIVES-lives)}\t\t🌟 {score}") 


def get_a_word(category = None):
    global all_words
    all_words = read_csv("data/words.csv")
    return random.choice(all_words)


def read_csv(fname, delimiter = ',', category = None):

    print(f"Reading from csv file: {fname} ...")

    words = []
    with open(fname) as file:
        reader = csv.DictReader(file, delimiter=delimiter)   # when we iterate over reader, each row will be of type dict.
        for row in reader:
            if category:
                if row['category'] == category:
                    words.append(row)
            else:
                words.append(row)

    return words

def write_to_file(fname, words, mode="a"):
    with open(fname, mode) as file:
        #file.write(f"{content}\n")
        writer = csv.DictWriter(file, fieldnames = words[0].keys()) 
        writer.writerows(words)

def print_score(score):

    scoreboard = f"""
 ______________
|              | 
      🌟 {score}
    Game Over.
|______________|
           |
   (\__/)  |
   (•ㅅ•)  ||
   /  　  づ
"""

    print(scoreboard)

if __name__ == "__main__":
    main()