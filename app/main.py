import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    user = input()
    print(f"{user}: command not found")

if __name__ == "__main__":
    main()
