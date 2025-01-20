# this is a simple program that takes a text input and counts the number of characters in the text

# import the needed modules
from gooey import Gooey, GooeyParser
from collections import Counter

@Gooey(program_name="Text Transformer and Character Counter", language="english")
def main():
    # Create a GooeyParser object
    parser = GooeyParser(description="Enter text to transform case and count characters.")
    
    # Add an input field for text
    parser.add_argument(
        "Text",
        help="Enter the text you want to process",
        type=str,
        widget="TextField",
    )

    # Parse the input
    args = parser.parse_args()
    user_input = args.Text

    # Convert text: swap lowercase and uppercase
    transformed_text = user_input.swapcase()

    # Count character repetitions
    char_counts = Counter(user_input)

    # Display transformed text
    print("Transformed Text:")
    print(transformed_text)

    # Display character counts
    print("\nCharacter Counts:")
    for char, count in char_counts.items():
        print(f"'{char}': {count} times")

if __name__ == "__main__":
    main()
