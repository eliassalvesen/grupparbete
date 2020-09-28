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
    endscore = float((100 * points) / user_rounds)
    print("your final score is", endscore, "%")
main()
