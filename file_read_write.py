# Author: Yasmin Opiyo

def modify_content(content: str) -> str:
    """
    Function to modify file content.
    Example: convert text to uppercase.
    """
    return content.upper()

def main():
    # Input and output filenames 
    input_file = "input.txt"
    output_file = "modified_output.txt"

    try:
        # Read content from file
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write to new file
        with open(output_file, 'w') as outfile:
            outfile.write(modified)

        print(f" Modified file saved as '{output_file}'")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
