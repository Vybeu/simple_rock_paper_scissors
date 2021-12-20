def rock_paper_scissors(choice, choice_two):
    choice = input("Please select your move: ")
    choice_two = input("Please select your move: ")
    if (choice == "rock" and choice_two == "scissors"):
        print("Player one wins!")
    elif (choice == "scissors" and choice_two == "paper"):
        print("Player one wins!")
    elif (choice == "paper" and choice_two == "rock"):
        print("Player one wins!")
    elif (choice == "rock" and choice_two == "rock"):
        print("Tie game!")
    elif (choice == "paper" and choice_two == "paper"):
        print("Tie game!")
    elif (choice == "scissors" and choice_two == "scissors"):
        print("Tie game!")
    elif (choice == "rock" and choice_two == "paper"):
        print("Player two wins!")
    elif (choice == "paper" and choice_two == "scissors"):
        print("Player two wins!")
    elif (choice == "scissors" and choice_two == "rock"):
        print("Player two wins!")
    else:
        print("invalid input!")


rock_paper_scissors("", "")
