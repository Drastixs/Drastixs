import sys

def runEchoCmd(args):
    print(" ".join(args))


def main():
    builtinCmds = {"echo":runEchoCmd,"exit":None,"type":None}
    while True:
        sys.stdout.write("$ ")
        user = input()
        userSplit = user.split(" ")
        cmd = userSplit[0]
        args = []
        if len(userSplit) > 1:
            args = userSplit[1:]
        commandIsBI = cmd in builtinCmds.keys()#whether command is builtin or not

        #start of command check
        if  commandIsBI: 
            func = builtinCmds[cmd]
            if func != None:
                res = func(args)
                continue#stop any other command running
            #else if func is none then pesummed to be in switch case steps

        if cmd == "exit":
            if (len(args) != 1):
                continue
            if args[0].isdigit():
                return args[0] 

        elif cmd == "type":
            if len(args) == 0:
                continue
            if args[0] in builtinCmds:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]}: not found")
        else:
            print(f"{user}: command not found")

if __name__ == "__main__":
    main()
