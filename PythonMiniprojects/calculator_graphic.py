# this is a simple calculator that takes two numbers and an operation and returns the result

# import the needed modules
from gooey import Gooey, GooeyParser

@Gooey(program_name="Math Operation Validator")
def main():
    # Create the Gooey Parser
    parser = GooeyParser(description="Enter your details and perform a math operation.")

    # User input fields
    parser.add_argument('Name', help="Enter your first name", type=str)
    parser.add_argument('Surname', help="Enter your surname", type=str)
    parser.add_argument('Number_1', help="Enter the first number (10-99)", type=int)
    parser.add_argument('Number_2', help="Enter the second number (10-99)", type=int)
    parser.add_argument(
        'Operation', 
        help="Choose the operation to perform", 
        choices=["Addition", "Subtraction", "Multiplication", "Division"]
    )

    # Parse the arguments
    args = parser.parse_args()

    # Validate inputs
    if not args.Name.strip() or not args.Surname.strip():
        print("Error: Name and surname cannot be empty.")
        return

    if not (10 <= args.Number_1 <= 99) or not (10 <= args.Number_2 <= 99):
        print("Error: Both numbers must be between 10 and 99.")
        return

    # Perform the selected operation
    if args.Operation == "Addition":
        result = args.Number_1 + args.Number_2
    elif args.Operation == "Subtraction":
        result = args.Number_1 - args.Number_2
    elif args.Operation == "Multiplication":
        result = args.Number_1 * args.Number_2
    elif args.Operation == "Division":
        if args.Number_2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = args.Number_1 / args.Number_2
    else:
        print("Error: Invalid operation.")
        return

    # Output the result
    print(f"Hello {args.Name} {args.Surname}, the result of {args.Operation.lower()} is: {result}")

if __name__ == "__main__":
    main()
