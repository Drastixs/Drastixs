import shlex

def main():
   cmd = "echo hello''world"
   print(shlex.split(cmd))  
    
if __name__ == "__main__": 
    main()