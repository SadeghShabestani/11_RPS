import random
import termcolor2

items = ["rock", "paper", "scissor"]
for item in items:
    print(f"Item: {item}")

user_score = 0
computer_score = 0

while True:
    user = input("Enter Choice: ")
    computer = random.choice(items)

    if user == "exit":
        break

    elif computer == "rock" and user == "paper":
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ User Wins _______", color="green"))
        user_score += 10
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "rock" and user == "scissor":
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ Computer Wins _______", color="red"))
        computer_score += 10
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "paper" and user == "rock":
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ User Wins _______", color="green"))
        user_score += 10
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "paper" and user == "scissor":
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ User Wins _______", color="green"))
        user_score += 10
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "scissor" and user == "rock":
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ User Wins _______", color="green"))
        user_score += 10
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == "scissor" and user == "paper":
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ Computer Wins _______", color="red"))
        computer_score += 10
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))

    elif computer == user:
        print(f"Compute_Choice: {computer}")
        print(termcolor2.colored("_______ Equal _______" ,color="blue"))
        print(termcolor2.colored(f"UserScore: {user_score} and ComputerScore: {computer_score}", color="yellow"))
