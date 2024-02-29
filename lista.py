print("Lista do Supermercado.")

lista1 = []

s = 0

for i in range(0,3):
    s += i
    pergunta = input("O que deseja adicionar a lista?\n")
    lista1.append(pergunta)

imprimir = input("Deseja ver os itens na lista? S/N\n")

if imprimir == 'S':
    print(f"Sua lista de compras:\n{lista1}")
elif imprimir == 'N':
    print('Até mais!')
else:
    print("Resposta errada reinicie o programa.")
