import random

def high_low_game():
    score = 0

    while True:
        # ランダムな2つの数字を生成
        current_num = random.randint(1, 10)
        next_num = random.randint(1, 10)

        print(f"Current number: {current_num}")
        user_choice = input("Will the next number be 'High' or 'Low'? (h/l): ").strip().lower()

        print(f"Next number: {next_num}")

        if (user_choice == 'h' and next_num > current_num) or (user_choice == 'l' and next_num < current_num):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Your score: {score}")
            break

    print(f"Game over. Your final score: {score}")

if __name__ == "__main__":
    high_low_game()



