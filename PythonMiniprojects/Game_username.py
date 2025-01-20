# This is a simple program that takes a username and a numeric password from two users and 
# conducts a 5-round guessing game between them. The program registers the users, validates the password, 
# and tallies the wins and losses in the game. The program uses the colorama library to display colored text 
# in the console.

# The program consists of the following steps:
# 1. Register two users by accepting a username and a numeric password.
# 2. Validate the password to ensure it contains numbers only.
# 3. Conduct a 5-round guessing game between the two users.
# 4. Display the results of the game, including the number of wins for each user and the overall winner.

# import the needed modules
import random
import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def register_user():
    """
    Registers a user by accepting a username and a numeric password.
    Exits if the password is invalid.
    """
    username = input("Enter your username: ")
    password = input("Enter your password (numbers only): ")

    if not re.fullmatch(r'\d+', password):
        print(Fore.RED + "Error: Password must contain numbers only. Exiting program.")
        exit()
    
    print(Fore.GREEN + f"Registration completed for user: {username}")
    return username

def play_guessing_game(user1, user2):
    """
    Conducts a 5-round guessing game between two users.
    Each user guesses a random number, and the game tallies wins/losses.
    """
    user1_score = 0
    user2_score = 0

    print(Fore.BLUE + "\nStarting the guessing game!")
    print(Style.BRIGHT + f"{user1} and {user2}, you will guess numbers 5 times.\n")

    for round_num in range(1, 6):
        print(Fore.YELLOW + f"Round {round_num}:\n")
        number_to_guess = random.randint(1, 10)
        
        for user in [user1, user2]:
            guess = int(input(Fore.CYAN + f"{user}, guess the number between 1 and 10: "))
            if guess == number_to_guess:
                print(Fore.GREEN + f"Correct! {user} guessed the number!")
                if user == user1:
                    user1_score += 1
                else:
                    user2_score += 1
            else:
                print(Fore.RED + f"Wrong! The correct number was {number_to_guess}.")
    
    print(Fore.MAGENTA + "\nGame Over! Final Results:")
    print(Style.BRIGHT + f"{user1}: {user1_score} wins")
    print(Style.BRIGHT + f"{user2}: {user2_score} wins")
    
    if user1_score > user2_score:
        print(Fore.GREEN + f"\n{user1} is the winner!")
    elif user2_score > user1_score:
        print(Fore.GREEN + f"\n{user2} is the winner!")
    else:
        print(Fore.YELLOW + "\nIt's a tie!")

# Main program
if __name__ == "__main__":
    print(Fore.CYAN + "User Registration:")
    user1 = register_user()
    user2 = register_user()

    play_guessing_game(user1, user2)

# if __name__ == "__main__":
# This line is a special condition in Python. Here's what it means:

# When you run the file directly:

# Example: python my_program.py.
# The code inside this if block will run.
# When you import the file into another file:

# Example: import my_program in another Python script.
# The code inside this block will not run automatically.
# Why do we use it?
# To separate functionality:
# Code inside if __name__ == "__main__": is for testing or running the program directly.
# Code outside it (like functions or classes) can still be imported and reused by other scripts.

# Example
# Imagine two scripts:

# my_script.py:
# def greet():
#     print("Hello!")
# if __name__ == "__main__":
#     greet()

# another_script.py:
# import my_script
# print("Running another script.")
# When you run my_script.py, you will see:
# Hello!
# When you run another_script.py, you will see:
# Running another script.

# Because the if __name__ == "__main__": block in my_script.py doesn't run when it's imported.


# what if i here write print (greet)

# If you write print(greet) in another_script.py, here's what will happen:

# my_script.py
# def greet():
#     print("Hello!")
# if __name__ == "__main__":
#     greet()

# another_script.py
# import my_script
# print("Running another script.")
# print(greet)

# Output when you run another_script.py
# Running another script.
# <function greet at 0x...>

# Explanation:
# print(greet) does not call the function. Instead, it prints information about the function itself:
# The <function greet at 0x...> tells you:
# greet is a function.
# The memory location (e.g., 0x...) where the function is stored.

# What to do if you want to call the function?
# Use parentheses to call the function:
# greet()

# This would actually execute the function, printing:

# Hello!


# so i dont need to print. but just call the function greet()

# Yes, exactly! If you want the function to execute and show its behavior 
# (e.g., print something or perform its tasks), you need to call the function using parentheses:


# greet()
# This tells Python to execute the function.

# Example:
# If you have the function:

# def greet():
#     print("Hello!")
# Calling greet() will output:
# Hello!

# If you only write print(greet), it won't call the function. Instead, it will print the function object itself (its memory location).

# So, to execute greet, always use parentheses like this:

# greet()




