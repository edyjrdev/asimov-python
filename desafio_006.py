# jogo adivinhar as capitais do brasil

import random

capitais_brasil = {
    "AC": "Rio Branco",
    "AL": "Maceió",
    "AP": "Macapá",
    "AM": "Manaus",
    "BA": "Salvador",
    "CE": "Fortaleza",
    "DF": "Brasília",
    "ES": "Vitória",
    "GO": "Goiânia",
    "MA": "São Luís",
    "MT": "Cuiabá",
    "MS": "Campo Grande",
    "MG": "Belo Horizonte",
    "PA": "Belém",
    "PB": "João Pessoa",
    "PR": "Curitiba",
    "PE": "Recife",
    "PI": "Teresina",
    "RJ": "Rio de Janeiro",
    "RN": "Natal",
    "RS": "Porto Alegre",
    "RO": "Porto Velho",
    "RR": "Boa Vista",
    "SC": "Florianópolis",
    "SP": "São Paulo",
    "SE": "Aracaju",
    "TO": "Palmas"
}

menu_saida = 'q'
num_tentativas = 0
num_acertos = 0

# embaralhar capitais
capital_keys = list(capitais_brasil.keys())
random.shuffle(capital_keys)

while True:
    opt = input('Escolha a opção (j-jogar, q-sair):')
    if opt == menu_saida:
        break
    elif opt not in ['j', 'q']:
        print('Opção inválida.')
        continue
    else:
        for uf in capital_keys:
            resposta = input(f'Qual é a capital do estado {uf}?\n')
            if resposta == capitais_brasil[uf]:
                print(f'Correto, a capital do {uf} é {capitais_brasil[uf]}.')
                num_acertos += 1
                capital_keys.remove(uf)
                random.shuffle(capital_keys)
                if not capital_keys:
                   opt = menu_saida
            else:
                print(f'Incorreto, {resposta} NÃO é a capital do {uf}.')
            num_tentativas += 1
            opt = input('Deseja continuar (s-sim, n-não):')
            if opt == 's':
                continue
            else:
                opt = menu_saida
                break
        if opt == menu_saida:
            break

print(f'Tentativas: {num_tentativas}')
print(f'Acertos: {num_acertos}')
print(f'Percentual de Acertos: {(num_acertos/num_tentativas * 100):.2f}')
print('Fim do jogo.')