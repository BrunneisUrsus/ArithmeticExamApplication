import random
result = 0
right = 0
task = 0
operation = ["+", "-", "*"]
description_level = None
while True:
    print("""With the first message, the program should ask for a difficulty level:
    1 - simple operations with numbers 2-9
    2 - integral squares 11-29""")
    level = input()
    if level == "1" or level == "2":
        break
    else:
        print("Incorrect format")
        continue
if level == "1":
    description_level = "simple operations with numbers 2-9"
    while task < 5:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operator = random.choice(operation)
        if operator == "+":
            print(f"{a} + {b}")
            result = a + b
            task += 1
        elif operator == "-":
            print(f"{a} - {b}")
            result = a - b
            task += 1
        elif operator == "*":
            print(f"{a} * {b}")
            result = a * b
            task += 1
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
                continue
            else:
                if answer == result:
                    print("Right!")
                    right += 1
                    break
                elif answer != result:
                    print("Wrong!")
                    break
elif level == "2":
    description_level = "integral squares 11-29"
    while task < 5:
        low = 11
        high = 29
        a = random.randint(low, high)
        result = pow(a, 2)
        print(a)
        task += 1
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Wrong format! Try again.")
                continue
            else:
                if answer == result:
                    print("Right!")
                    right += 1
                    break
                elif answer != result:
                    print("Wrong!")
                    break
print(f"Your mark is {right}/5. Would you like to save the result? Enter yes or no.")
save = input()
yes = ["yes", "y"]
no = ["no", "n"]
if save.lower() in yes:
    print("What is your name?")
    name = input()
    test_result = f"{name}: {right}/5 in level {level} ({description_level}.)"
    with open("results.txt", "a") as mark:
        mark.write(test_result)
        mark.close()
        print("The results are saved in \"results.txt\".")
elif save.lower() in no:
    quit()
