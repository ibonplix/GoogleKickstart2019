#Google kickstart 2020 round a "Plates"

cases = 0
testcases = int(input())
while cases != testcases:
    suma2=0
    spb2=[]
    spb=[]
    cases += 1
    var=1
    variables = input().split()
    array=[]
    stacknum=(variables[0])
    stacknum=int(stacknum)
    platenum=(variables[1])
    plateswantednum=(variables[2])
    pwm=int(plateswantednum)
    stacksplatesbeauty=[]
    for i in range((stacknum)):
        stacksplatesbeauty.append(input().split())
    for i in range(len(stacksplatesbeauty)):
        array=(stacksplatesbeauty[i])
        spb=[]
        for i in range(len(array)):
            spb.append(int(array[i]))
        spb2.append(spb)
    #print(len(spb))
    print(spb2)    
    for i in range(len(spb2)):
            print(spb2[i])
            stack=spb2[i]
            for i in range(len(stack)):
                if var == 1:
                    suma=sum(stack[:(i+1)])
                    sumas=suma+suma2
                    print(sumas)
                    var=0
                if var == 0:
                    suma=sum(stack[:(i+2)])
                    sumas=suma+suma2
                    print(sumas)
                    var=1
            suma2=suma
    #beauty.append(sum())

    #print("Case #"+str(cases)+": "+str(  ))
