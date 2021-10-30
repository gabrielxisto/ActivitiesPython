medidor = float(input("Diga a temperatura: "))

if medidor <= 37.0:
    cancela = True
elif medidor > 37.0:
    cancela = False
## RESULTADO DA CANCELA
if cancela == True:
    print("Liberado!")
elif cancela == False:
    print("Você não esta autorizado a entrar!")