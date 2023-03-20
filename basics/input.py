# import colors
RED = "\033[31m"
GREEN = "\033[32m"
ENDC = '\033[0m'

def main():
    
    avg = avg_scores()
    print(f"{avg=}")



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