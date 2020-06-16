#google kickstart 2019 round a "Parcels"
from itertools import combinations
import numpy
import math as m


def dist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
cases = 0
testcases = int(input())
while cases != testcases:
    grid = []
    rowgrid = []
    unposfinal2=[]
    gridsize = input().split()
    rows=(gridsize[0])
    rows=int(rows)
    columns=(gridsize[1])
    for i in range(rows):
        rowval = input()
        grid=[]
        for i in range( len(rowval) ):
            grid.append(int(rowval[i]))
        rowgrid.append(grid)
    for i in range(len(rowgrid)):
        for j in range(len(rowgrid)):
            unpos=[]
            if rowgrid[i][j] == 1:
                unposfinal = []
                r1=i+1
                c1=j+1
                unpos=[r1]
                unposfinal.append(unpos)
                unpos=[c1]
                unposfinal.append(unpos)
                unposfinal2.append(unposfinal)
    #print (len(unposfinal))
    comb = (list((combinations(unposfinal2, 2))))
    lengthcom = len(comb)
    sumadistancias=[]
    for i in range(lengthcom):
        comb2=(comb[i])
        for i in range (len(comb2)):
            comb3=(comb2[0])
            for i in range (len(comb3)):
                r1=((comb3[0])[0])
                c1=((comb3[1])[0])

            comb4=(comb2[1])
            for i in range (len(comb3)):
                r2=((comb4[0])[0])
                c2=((comb4[1])[0])
        z = (abs(r1 - r2) + abs(c1 - c2))
        sumadistancias.append(z)
        minoveralldist=max(sumadistancias)
        print(f"r1,c1: ({r1},{c1}) r2,c2: ({r2},{c2})")
    cases += 1
    print(sumadistancias)
    print (minoveralldist)
    
    
    
