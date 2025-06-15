# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop to control the rows
while row < size:
    # Inner for loop to print asterisks in each column
    for col in range(size):
        print("*", end="")  # Print without a newline
    print()  # Newline after each row
    row += 1
