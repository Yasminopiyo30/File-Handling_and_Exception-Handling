# Author: Yasmin Opiyo

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
            print(" File content successfully read:")
            print(content)

    except FileNotFoundError:
        print(" Error: The file was not found. Please check the filename and try again.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
