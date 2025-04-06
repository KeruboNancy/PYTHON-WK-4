#QUESTION 1


# # Step 1: Define the input and output filenames
input_file = "input.txt"
output_file = "output.txt"

try:
    # Step 2: Open the input file for reading
    with open(input_file, "r") as file:
        content = file.read()

    # Step 3: Modify the content (e.g., convert text to uppercase)
    modified_content = content.upper()

    # Step 4: Write the modified content to the output file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"Modified content has been written to {output_file}")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except IOError:
    print(f"Error: Unable to read or write files.")




    #QUESTION 2


    # Step 1: Ask the user for the filename
filename = input("Enter the name of the file to read: ")
try:
    # Step 2: Attempt to open and read the file
    with open(filename, "r") as file:
        content = file.read()  # Read the entire content of the file
# Step 3: Display the content of the file
    print(f"\nContents of '{filename}':\n{content}")

except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")

except PermissionError:
    # Handle the case where the user does not have permission to read the file
    print(f"Error: You do not have permission to read the file '{filename}'.")

except IOError:
    # Handle other I/O-related errors
    print(f"Error: An unexpected I/O error occurred while trying to read '{filename}'.")