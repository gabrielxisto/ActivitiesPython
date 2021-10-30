import sys
import time
import random


idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade, portanto não pode participar do sorteio!")
    time.sleep(3)
    sys.exit()
else: 
    a = int(input("Digite o primeiro numero: "))
    b = int(input("Digite o segundo numero: "))
    c = int(input("Digite o terceiro numero: "))
    d = int(input("Digite o quarto numero: "))
    e = int(input("Digite o quinto numero: "))
    f = int(input("Digite o sexto numero: "))
    seusNumeros = a,b,c,d,e,f
    x1 = random.randint(1,20)
    x2 = random.randint(1,20)
    x3 = random.randint(1,20)
    x4 = random.randint(1,20)
    x5 = random.randint(1,20)
    x6 = random.randint(1,20)
    x10 = x1,x2,x3,x4,x5,x6
    print("Seu numero: ",seusNumeros)
    print("Numero sorteado: ",x10)
    time.sleep(4)
    if seusNumeros == x10:
        print("Você ganhou!")
    else:
        print("Você não ganhou!")
    