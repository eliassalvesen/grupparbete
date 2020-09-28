import random
def calculation(value1, value2, user_answer, points, game_level):
    true_answer = value1 * value2
    if user_answer == true_answer:
        print("your answer was correct, the difficulty is going up!")
        points += 1
        game_level += 1
    else:
        print("your answer was not correct!")
        print("the correct answer was", true_answer)
    return points, game_level


def procent(points, user_rounds):
    x = round((points / user_rounds) * 100)
    if x == 100:
        return "100% correct"
    elif 99 > x > 80:
        return "80-99% correct"
    elif 79 > x > 60:
        return "60-79% correct"
    elif 59 > x > 40:
        return "40-59% correct"
    elif 39 > x > 20:
        return "20-39% correct"
    elif 19 > x >= 0:
        return "0-19% correct"


def main():
    points = 0
    game_level = int(input("What level?\n 5: 5 * 5\n10: 10 * 10\n20: 20 * 20\n"))
    user_rounds = int(input("How many rounds? "))
    for i in range(0, user_rounds):
        n1 = random.randint(1, game_level)
        n2 = random.randint(1, game_level)
        print("what is", n1, "*", n2,"?")
        user = int(input("your answer: "))
        points, game_level = calculation(n1, n2, user, points, game_level)
    endscore = procent(points, user_rounds)
    print("your final score is", endscore)
main()
