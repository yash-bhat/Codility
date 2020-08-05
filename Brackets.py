# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    braces = {'[':']','{':'}','(':')'}
    
    open = []
    
    if S == '':
        return 1
    
    if (S[0] not in braces.keys()) or (len(S)%2!=0):
        return 0
        
    for s in S:
        if s in braces.keys():
            open += s
        else:
            if (open != []) and (s == braces[open[-1]]):
                open.pop()
            else:
                return 0
    
    if open == []:
        return 1
    else:
        return 0
