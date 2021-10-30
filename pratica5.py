indicePol = float(input("Digite o indice: "))
if indicePol < 0.25: 
    print("Tudo bem todos podem prosseguir!")
elif indicePol > 0.30 and indicePol < 0.40:
    print("Grupo 1 deve suspender suas atividades")
elif indicePol > 0.40 and indicePol < 0.50:
    print("Grupo 1 e 2 deve suspeder suas atividades")
else:
    print("Todos os grupos devem parar suas atividades")