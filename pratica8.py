produto1 = float(input("Digite o valor do produto: "))
produto2 = float(input("Digite o valor do produto: "))
produto3 = float(input("Digite o valor do produto: "))

if produto1 < produto2 and produto1 < produto3: 
    print("Você deve comprar o Produto 1")
elif produto2 < produto1 and produto2 < produto3:
    print("Você deve comprar o Produto 2")
elif produto3 < produto2 and produto2 < produto1:
    print("Você deve comprar o Produto 3")