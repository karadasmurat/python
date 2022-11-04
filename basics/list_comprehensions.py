# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

def main():


    numbers = range(10)

    first_5 = [num for num in numbers if num < 5]
    print(*numbers)
    print(*first_5)

    results = [
        {"name":"Bob", "score":33},
        {"name":"Foo", "score":90},
        {"name":"Bar", "score":85},
        {"name":"Baz", "score":100}
    ]

    # filter the results
    # ------ version 1 ---------
    grades_A = []
    for result in results:
        if result['score'] >= 85:
            grades_A.append(result['name'])
    print(f"{grades_A=}")

    # ------ version 2 ---------
    grades_F = [result['name'] for result in results if result['score'] < 60]
    print(f"{grades_F=}")



if __name__ == "__main__":
    main()