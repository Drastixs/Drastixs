import sys


def main():
    while True:
        sys.stdout.write("$ ")
        user = input()
        print(f"{user}: command not found")
        userSplit = user.split(" ")
        cmd = userSplit[0]
        args = []
        if len(userSplit) > 1:
            args = userSplit[1:]
        if cmd == "exit":
            if (len(args) != 1):
                continue
            if args[0].isdigit():
                return args[0] 

if __name__ == "__main__":
    main()
