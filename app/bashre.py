PARSE_VALID = 0
PARSE_INVALID = 1
PARSE_CONTAIN_STRING_CHAR_IN_ARG = 2#if a "'" character is found in the middle of an argument it is invalid


def parseBashString(bashStr):
    args = []
    isStr = False#whether the current character is in a literal string block
    currArg = ""
    for char in bashStr:
        if char == '\'':#inverts current state of isStr
            if not isStr and len(currArg) > 0:
                return 1, "" 
            isStr = not isStr