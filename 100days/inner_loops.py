reps = [10, 3, 7, 5, 8]

for rep in reps:
    # print(rep * "*")      # pytonian way, string repetition
    for col in range(rep):
        print("#", end="")
    print() 