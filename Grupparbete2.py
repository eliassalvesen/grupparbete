import random


def calculation(value1, value2, user_answer, points, game_level):
    true_answer = value1 * value2
    if user_answer == true_answer:
        print("Your answer was correct, the difficulty is going up!")
        points += 1
        game_level += 1
    else:
        print("Your answer was not correct!")
        print("the correct answer was", true_answer)
    return points, game_level


def procent(points, user_rounds):
    x = round((points / user_rounds) * 100)
    if x == 100:
        return "100%"
    elif 99 > x > 80:
        return "80-99%"
    elif 79 > x > 60:
        return "60-79%"
    elif 59 > x > 40:
        return "40-59%"
    elif 39 > x > 20:
        return "20-39%"
    elif 19 > x >= 0:
        return "0-19%"


def gameDifficulty(choice):
    if choice == 1:
        return 5
    elif choice == 2:
        return 10
    elif choice == 3:
        return 20
    else:
        print("Please select only between numbers 1-3")
        main()


def main():
    points = 0
    game_level = int(input("Select difficulty level\n1 = Easy\n2 = Medium\n3 = Hard\n"))
    game_level = gameDifficulty(game_level)
    user_rounds = int(input("How many rounds? "))
    for i in range(0, user_rounds):
        n1 = random.randint(1, game_level)
        n2 = random.randint(1, game_level)
        print("What is", n1, "*", n2, "?")
        user = int(input("Your answer: "))
        points, game_level = calculation(n1, n2, user, points, game_level)

    endscore = procent(points, user_rounds)
    print("Your final score is", points, "/", user_rounds, "correct,", endscore)


main()
