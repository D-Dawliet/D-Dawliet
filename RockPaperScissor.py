import random

user_score = 0
computer_score = 0

while True:
    List = ["rock", "paper", "scissor"]
    user_input = input("To play type(rock/paper/scissor) or 'q' to quit- \n:").lower()
    if user_input == "q":
        quit()

    if user_input not in List:
        print("Invalid Input")
        continue

    computer_choice = random.choice(List).lower()
        
    if user_input == "scissor" and computer_choice == "paper":
        print("computer: ", computer_choice)
        print("You won!")
        user_score += 1
        print("Your score: ", user_score)
        print("Computer score: ", computer_score)
    elif user_input == "paper" and computer_choice == "rock":
        print("computer: ", computer_choice)
        print("You won!")
        user_score += 1
        print("Your score: ", user_score)
        print("Computer score: ", computer_score)
    elif user_input == "rock" and computer_choice == "scissor":
        print("computer: ", computer_choice)
        print("You won!")
        user_score += 1
        print("Your score: ", user_score)
        print("Computer score: ", computer_score)
    elif user_input == computer_choice:
        print("computer: ", computer_choice)
        print("Draw")
        print("Your score: ", user_score)
        print("Computer's score: ", computer_score)
    else:
        print("computer: ", computer_choice)
        print("Computer won!")
        computer_score += 1
        print("Your score: ", user_score)
        print("Computer's score: ", computer_score)
