# Dado duas listas, printe todos os valores 
# que aparecem duplicados nas duas listas

lista_01 = [10, 22, 34, 56, 89, 20, 100, 1, 34]
lista_02 = [11, 23, 44, 56, 189, 21, 100, 1]

print('Desafio 001')
for elemento in lista_01:
    for elemento_02 in lista_02:
        if elemento == elemento_02:
            print(f'Elemento duplicado: {elemento}')

# Dado duas listas, printe uma mensagem dizendo se existe 
# algum elemento em comum entre elas ou não.
print('-' * 30)
print('Desafio 002')
existe_elemento_comum = False
for elemento in lista_01:
    if elemento in lista_02:
        print(f'Elemento comum: {elemento}')
        existe_elemento_comum = True
        break