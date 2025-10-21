import sys


def main():
    while True:
        sys.stdout.write("$ ")
        user = input()
        print(f"{user}: command not found")

if __name__ == "__main__":
    main()
