# import the Gooey library
from gooey import Gooey, GooeyParser

# the decorator provided by the Gooey library: @Gooey()
# What is a Decorator?
# A decorator modifies or enhances the behavior of a function or class without changing its actual code.
# The @Gooey decorator modifies the behavior of the main() function by adding a graphical user interface (GUI) to it.

@Gooey(program_name="Odd or Even Checker")

def main():
    # Create the Gooey Parser
    parser = GooeyParser(description="Enter 4 numbers to check if they are odd or even.")
    
    # Add arguments for the 4 numbers
    parser.add_argument('Number_1', type=int, help="Enter the first number")
    parser.add_argument('Number_2', type=int, help="Enter the second number")
    parser.add_argument('Number_3', type=int, help="Enter the third number")
    parser.add_argument('Number_4', type=int, help="Enter the fourth number")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Extract the numbers and check odd/even
    numbers = [args.Number_1, args.Number_2, args.Number_3, args.Number_4]
    results = ["Even" if num % 2 == 0 else "Odd" for num in numbers]
    
    # Display the results in the console
    print("Results:")
    for i, (num, result) in enumerate(zip(numbers, results), start=1):
        print(f"Number {i} ({num}) is {result}")

if __name__ == "__main__":
    main()


# zip is a Python function that pairs elements from two iterables
# (e.g., lists, tuples) together into a single iterable of tuples.

# In this case:
# numbers contains the user-input numbers (e.g., [5, 10, 7, 12]).
# results contains the odd/even result for each number (e.g., ["Odd", "Even", "Odd", "Even"]).
# Result of zip(numbers, results)