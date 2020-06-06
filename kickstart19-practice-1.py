import random
import time

true=1
while true==1:
    time.sleep(1)
    #minimo = int(input("Número minimo: "))
    #maximo = int(input("Número máximo: "))
    minimo = (random.randint(0,100000000))
    maximo = (random.randint(0,100000000))
    if maximo == minimo:
        break
    if maximo < minimo:
        var = maximo
        maximo = minimo
        minimo = var
    print(f"Número minimo: {minimo}")
    print(f"Número máximo: {maximo}")
    rdn = (random.randint(minimo+1,maximo-1))
    #rdn = 30
    print(f"RANDOMNUMBER: {rdn}")
    niten=0
    ntries = 30
    maximo
    minimo
    intento = int((maximo-minimo)/2)
    while ntries != 0:
        niten+=1
        ntries -= 1
        print(f"INTENTO Nº {niten}: {intento}")
        if intento == rdn:
            print("Acertaste!")
            break
        if intento < rdn:
            minimo=intento
            intento=(int((maximo-minimo)/2)+minimo)
        elif intento > rdn:
            maximo=intento
            intento=(int((maximo-minimo)/2)+minimo)
        

    

        
