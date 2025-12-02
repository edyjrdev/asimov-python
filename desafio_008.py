# Simulador de Baralho
# Emoji de Naipe: ♠️♥️♦️♣️🃏
import random as rd

simbolos = list('A23456789') + ['10'] + list('JQK')
naipes = ['♠️', '♥️', '♦️', '♣️']
coringa = '🃏'
num_jogadores=0


def gerar_baralho(num_baralho=2, com_coringa=False, num_coringa=0):
    baralho = []
    for i in range(num_baralho):
        for naipe in naipes:
            for simbolo in simbolos:
                carta = simbolo + naipe
                baralho.append(carta)
        if com_coringa:
            if num_coringa > 0:
                for i in range(num_coringa):
                    baralho.append(coringa) 
    return baralho

def embaralhar_baralho(baralho):
    rd.shuffle(baralho) # embaralha lista e retorna None

def distribuir_carta(novo_baralho, mao_jogador):
    num_carta_jogador = 5
    for carta in range(num_carta_jogador):
        mao_jogador.append(novo_baralho.pop())
    mao_jogador.sort()

def mostrar_baralho(baralho):
    print(f'Cartas no baralho:{len(baralho)}')
    print('-'*30)
    print(' | '.join(baralho))

# maos dos jogadores
mao_jogador01 = []
mao_jogador02 = []
mao_jogador03 = []
mao_jogador04 = []

#novo_baralho = gerar_baralho() # baralho padrão
novo_baralho = gerar_baralho(num_baralho=2, com_coringa=True, num_coringa=2)

print(f'Gerar baralho com {len(novo_baralho)}')
print('Embaralhar')
embaralhar_baralho(novo_baralho) # embaralha lista por referencia
mostrar_baralho(novo_baralho)

print('Distribuir cartas')
distribuir_carta(novo_baralho, mao_jogador01)
distribuir_carta(novo_baralho, mao_jogador02)
distribuir_carta(novo_baralho, mao_jogador03)
distribuir_carta(novo_baralho, mao_jogador04)
print(f'Jogador 01:{mao_jogador01}')
print(f'Jogador 02:{mao_jogador02}')
print(f'Jogador 03:{mao_jogador03}')
print(f'Jogador 04:{mao_jogador04}')
print('Monte')
mostrar_baralho(novo_baralho)