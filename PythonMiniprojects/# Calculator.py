# this is a calculator python program that performs basic arithmetic operations
# such as addition, subtraction, multiplication, division, square root, and exponentiation.
# The program displays a menu of operations for the user to choose from.
# The user can select an operation by entering a number from 0 to 6.
# The program then asks for the necessary inputs and performs the operation.
# The result and the execution time of the operation are displayed.
# The calculator runs continuously unless the user chooses to exit by selecting 0.


# import the needed modules
import time  # to measure the execution time of operations 
import math  # to perform mathematical operations

# Function to display the menu
def display_menu():  # The display_menu function prints the list of available operations for the user to choose from.
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Exponentiation (^)")
    print("0. Exit")

# Perform calculations and measure execution time
def calculate():
    while True:     # The calculator runs continuously unless the user chooses to exit by selecting 0.
        display_menu()
        try:        # The user selects an operation by entering a number from 0 to 6.
            choice = int(input("Enter your choice (0-6): "))           
            if choice == 0:  # If the user enters 0, the program displays a goodbye message and exits the loop using break.
                print("Exiting the calculator. Goodbye!")
                break

            start_time = time.time()  # Start timing. The time.time() function measures the start and end of each operation.
            # For operations involving two numbers (like addition, subtraction ect.), the program aks for two inputs.
            if choice in [1, 2, 3, 4, 6]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == 1:
                    result = num1 + num2
                    operation = "Addition"
                elif choice == 2:
                    result = num1 - num2
                    operation = "Subtraction"
                elif choice == 3:
                    result = num1 * num2
                    operation = "Multiplication"
                elif choice == 4:
                    if num2 == 0: # Division by zero is prevented with a check.
                        print("Error: Division by zero is undefined.")
                        continue
                    result = num1 / num2
                    operation = "Division"
                elif choice == 6:
                    result = num1 ** num2
                    operation = "Exponentiation"

            elif choice == 5:
                num = float(input("Enter the number: "))
                if num < 0: # Square root of negative numbers is disallowed.
                    print("Error: Square root of a negative number is undefined.")
                    continue
                result = math.sqrt(num)
                operation = "Square Root"
            else: # If the user enters a number outside 0-6, the program displays an error and goes back to the menu.
                print("Invalid choice. Please select a valid option.")
                continue
            
            end_time = time.time()  # End timing
            
            # Display the result and execution time
            print(f"\nOperation: {operation}")
            print(f"Result: {result}")
            
            # Subtract start_time from end_time to get the total time
            # with .8f we can round the numbers (in this case, 8 decimal places)
            print(f"Execution Time: {end_time - start_time:.8f} seconds")

            #If the user enters something invalid (like letters instead of numbers)
            # the program displays an error and prompts again.
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Run the calculator
calculate()
