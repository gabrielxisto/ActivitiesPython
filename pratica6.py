golsTime1 = int(input("Digite o numero de gols do Time 1: "))
golsTime2 = int(input("Digite o numero de gols do Time 2: "))

if golsTime1 > golsTime2: 
    print("Time um ganhou!")
elif golsTime2 > golsTime1:
    print("Time dois ganhou!")
elif golsTime2 == golsTime1: 
    print("EMPATE")