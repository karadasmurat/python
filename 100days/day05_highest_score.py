#  Python will only find your file if your file is in the systems path. 
# import sys
# sys.path.append('../')
# import colors

RED = "\033[31m"
ENDC = '\033[0m'

scores = input("Input a list of student scores, ie. 70 90 80: ").split()

max_score = 0
for score in scores:
    try:
        score = int(score)
        if(score > max_score):
            max_score = int(score)
    except ValueError:
        # raise ValueError("BAD INPUT");
        print(f"{RED}Error: Scores should be seperated, ie. 70 80 90{ENDC}")
        exit(0)

print("The highest score in the class is:", max_score)

# In Python, there is a built-in function max() you can use to find the largest number in a list.
print("Pytonic way:", max(scores))