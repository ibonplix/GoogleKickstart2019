cases = 0
testcases = int(input())
while cases != testcases:
    variables = input().split()
    sessions=(int(variables[0]))
    additional=(int(variables[1]))
    minutesperses = input().split()
    minutespersesint=[]
    for i in range(len(minutesperses)):
        minutespersesint.append(int(minutesperses[i]))
    print(sessions)
    print(additional)
    print(minutespersesint)
    cases += 1
    
