preco = float(input("Digite aqui o preço do produto: "))
desconto = (preco/100)*5
total = preco - desconto
print("O novo valor com o desconto ficou: {}".format(total))
