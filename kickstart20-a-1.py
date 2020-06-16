#Google kickstart 2020 round a "Allocation"
from itertools import combinations

cases = 0
testcases = int(input())
while cases != testcases:
    numcasas=[]
    pricesint=[]
    cases += 1
    variables = input().split()
    n=(variables[0])
    b=(variables[1])
    prices = input().split()
    for i in range(len(prices)):
        pricesint.append(int(prices[i]))
    for i in range(len(pricesint)):
        comb = (list((combinations(pricesint, i))))
        for i in range(len(comb)):
            if (sum(comb[i])) <= int(b):
                numcasas.append(len(comb[i]))
    print("Case #"+str(cases)+": "+str(max(numcasas)))
    
#Tiempo necesitado: 15:40 (minutos,segundos)
