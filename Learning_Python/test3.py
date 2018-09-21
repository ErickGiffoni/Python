compras = []
while True :
    product = input("Product : ")
    if product == 'fim' :
        break
    quantidade = int(input("Quantidade : "))
    price = float(input('Preco : '))
    compras.append([product, quantidade, price])
soma = 0.0
for e in compras :
    print("%20s||x%5d||%5.2f||%6.2f||" %(e[0], e[1],e[2], e[1]*e[2]))
    soma += e[1]*e[2]
print("Total = %7.2f" %soma)
