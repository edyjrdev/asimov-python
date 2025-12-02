# cifra de cesar

alfabeto ='abcdefghijklmnopqrstuvwxyz'

mensagem_cifrada = []

print('Cifra de Cesar')
mensagem = input('Informe a mensagem a ser cifrada: ')
chave = int(input('Informe a chave utilizada (int): '))

for letra in mensagem:
    letra = letra.lower()
    if letra not in alfabeto:
        mensagem_cifrada.append(letra)
        continue
    else:
        ind_letra = alfabeto.find(letra)
        deslocamento = chave + ind_letra

        # deslocamento real tem que ficar entre 0 e 25
        if deslocamento < 26:
            mensagem_cifrada.append(alfabeto[deslocamento])
        else:
            mensagem_cifrada.append(alfabeto[26-deslocamento])
mensagem_cifrada= "".join(mensagem_cifrada)
print(f'Mensagem original: {mensagem}')
print(f'Mensagem cifrada: {mensagem_cifrada}')
