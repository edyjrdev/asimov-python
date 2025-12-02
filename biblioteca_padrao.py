import math
import datetime as dt
import random as rd
import os 
import time

def sorteia_mega():
    dezenas = set()
    for _ in range (1, 7):
        dezenas.add(rd.randint(1,60))
    return dezenas

def calcula_perimitro_circulo(raio=1):
    return 2 * math.pi * raio

inicio = dt.datetime.now()
inicio_seg = time.time()

print(inicio)
raio = float(input('Digite o raio de um circulo: '))

print(f'Perimetro = {calcula_perimitro_circulo(raio)}')

agora = dt.datetime.now()
print(agora)
print(sorteia_mega())

alunos = ['Edy', 'Sara', 'Laila','Zig', 'Rafik','Peka', 'Greta']

for _ in range(3):
    time.sleep(1)
    print(f'{_+1}.Sorteado:{rd.choice(alunos)}')

print(os.getcwd())
print(os.listdir())

final_seg = time.time()

print(f'tempo transcorrido: {agora - inicio}')
print(f'segundos transcorridos:{final_seg-inicio_seg:.2f}')