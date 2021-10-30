anonascimentoEmp = int(input("Digite o nascimento do empregado: "))
ingressEmp = int(input("Digite a data de ingressão: "))
nossoAno = int(input("Digite o ano que você esta: "))

idade = nossoAno-anonascimentoEmp
tempTrabalho = nossoAno-ingressEmp

print("Idade: ",idade,"Anos ")
print("Tempo de trabalho: ",tempTrabalho,"Anos ")

if idade >= 60 and tempTrabalho >= 25:
    print("Requerer aposentadoria")
else: 
    print("Não querer")