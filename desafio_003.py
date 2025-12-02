# Calcular soma e media de sequencia de numeros

print('Desafio 1.1')
numeros = list(range(1, 11))

soma = 0
media = 0

for numero in numeros:
    soma += numero
media = soma / len(numeros)

print(f'Soma: {soma}')
print(f'Media: {media}')

print('-' * 30)
print('Desafio 1.2')
valores = [10, 33, 22, 55, -9, 99, 500, 121, 0, 231, 1, 222, 432]
maior_valor = valores[0]
for valor in valores:
    if valor > maior_valor:
        maior_valor = valor
print(f'Maior valor: {maior_valor}')

print('-' * 30)
print('Desafio 1.3')
palavras = ['python', 'java', 'php', 'javascript', 'c# ', 'visual basic', 'ruby', 'pear']
max_caracteres = 4

for palavra in palavras:
    if len(palavra) >= max_caracteres:
        print(f'Palavra: {palavra} com mais de {max_caracteres} caracteres.')