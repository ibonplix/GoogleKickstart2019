#google kickstart 2019 round a "Training"
from itertools import combinations

cases = 0
testcases = int(input())
while cases != testcases:
    studentsplayers = input().split()
    list_of_skills = input().split()
    x = 0
    pos = 0
    cases += 1
    students = studentsplayers[0]
    players = int(studentsplayers[1])
    comb = (list((combinations(list_of_skills, players))))
    lengthcom = len(comb)
    lowestdiff = []
    for i in range(lengthcom):
        combsort = list(comb[i])
        combsort = sorted(list(map(int, combsort)))
        lengthsort = ((len(combsort))-1)
        for i in range(lengthsort):
            x += ((max(combsort)) - (combsort[i]))
        lowestdiff.append(x)
    print(f"Case #{cases}: {lowestdiff[0]}")
        

            
            
            
