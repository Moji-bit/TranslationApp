# this a chance game
# The game generates a random number between 1 and 100 and asks the user to guess the number.
# The game provides hints to the user if the guessed number is greater or less than the random number.

# import the needed modules

# randint: to generate random integers.
from random import randint

# colorama:  to add color and styling to the text printed to the console.
from colorama import Fore, Style, init

# Fore: for text color (Fore.YELLOW, Fore.GREEN).
# Style: for the style of the text, like Style.RESET_ALL.

# This initializes the colorama library and ensures the color output works.
init()

def random_game():
    #The game starts with a welcome message displayed in yellow (Fore.YELLOW)
    # and the color is reset after the message (Style.RESET_ALL).
    print(f"{Fore.YELLOW}Welcome to the Random Number Guessing Game!{Style.RESET_ALL}")
    
    guessed_numbers = []  # A list to store all the numbers that the user guesses.
    random_numbers = []   # A list to store the randomly generated numbers corresponding to each guess.

    while True: #The game runs in a while loop that continues until the user exits by entering -1.
        try:
            # User enters a guessed number and input is converted to an integer using int().
            guessed_number = int(input("Enter your guessed number (or -1 to exit): "))
            
            # If the user inputs -1, the game will exit and print a thank you message.
            if guessed_number == -1:
                print(f"{Fore.CYAN}Exiting the game. Thank you for playing!{Style.RESET_ALL}")
                break
            
            # Generate a random number between 1 and 100
            random_number = randint(1, 100)

            # Store numbers in lists
            guessed_numbers.append(guessed_number)
            random_numbers.append(random_number)


            # If the random number is greater than the guessed number, 
            # it prints the random number in green with comparison (gt).
            if random_number > guessed_number:
                print(f"{Fore.GREEN}Random number: {random_number} (gt){Style.RESET_ALL}")
                print(f"Your guess: {guessed_number}")
                
            # If the random number is less than the guessed number, 
            # it prints the random number in red with comparison (lt).
            elif random_number < guessed_number:
                print(f"{Fore.RED}Random number: {random_number} (lt){Style.RESET_ALL}")
                print(f"Your guess: {guessed_number}")
                
            # If the random number equals the guessed number,
            # it prints the random number in blue and writes "Equal"
            else:
                print(f"{Fore.BLUE}Random number: {random_number} (Equal){Style.RESET_ALL}")
                print(f"Your guess: {guessed_number}")

        # If the user enters anything other than a valid integer, 
        # an error message is printed in magenta
        except ValueError:
            print(f"{Fore.MAGENTA}Invalid input! Please enter a valid number.{Style.RESET_ALL}")

        # After the game loop ends, guessed_numbers and random_numbers lists are converted to tuples.
        guessed_numbers_tuple = tuple(guessed_numbers)
        random_numbers_tuple = tuple(random_numbers)

        # Display the stored numbers as tuples
        print("\nSummary:")
        print(f"{Fore.YELLOW}Guessed Numbers (tuple): {guessed_numbers_tuple}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Random Numbers (tuple): {random_numbers_tuple}{Style.RESET_ALL}")

# Run the game
random_game()