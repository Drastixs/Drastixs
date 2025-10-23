import sys
import os
import subprocess

PATH = os.environ["PATH"]
HOME = os.environ["HOME"]

def findExecFile(searchCmd):
    paths = PATH.split(":")
    for path in paths:
        if not os.path.exists(path):
            continue
        for entry in os.listdir(path):
            if os.path.isdir(entry):
                continue
            if entry != searchCmd:
                continue
            if not os.access(os.path.join(path,entry),os.X_OK):#ensures execution permission below
                break
            return os.path.join(path,entry)
    return None

def runEchoCmd(args):
    print(" ".join(args))

def runPwdCmd(args):
    print(os.getcwd())

def runCdCmd(args):
    if len(args) == 0:
        return 1
    path = str(args[0])
    if path.startswith("~"):
        if (len(path) > 1):
            path = HOME#incase it is just ~ as the argument
        else:
            path = os.path.join(HOME,path[1:])#join current working directory and path
            
    absPath = os.path.abspath(path)
    if not os.path.exists(absPath):
        print(f"cd: {args[0]}: No such file or directory")
        return 1
    os.chdir(absPath)

def runTypeCmd(args):
    if len(args) == 0:
        return 1
    searchCmd = args[0]#cmd we are searching for 
    if args[0] in builtinCmds:
        print(f"{args[0]} is a shell builtin")
        return 0
    
    exePath = findExecFile(searchCmd)

    if exePath == None: 
        print(f"{searchCmd}: not found")
        return 1
    
    print(f"{searchCmd} is {exePath}")
    return 0
         
builtinCmds = {"echo":runEchoCmd,"cd":runCdCmd,"pwd":runPwdCmd,"exit":None,"type":runTypeCmd}

def main():
    while True:
        sys.stdout.write("$ ")
        user = input().strip()#removes start and ending spaces
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
                return 0
            if args[0].isdigit():
                return args[0] 

        pathToExec = findExecFile(cmd)
        if pathToExec != None:
            args.insert(0,cmd)
            subprocess.run(args)
            continue
        
            
        print(f"{user}: command not found")

if __name__ == "__main__":
    main()
