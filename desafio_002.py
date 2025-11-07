# 03 tentativas para descobrir um numero secreto

# config
NUM_SECRETO = 10
MAX_TENTATIVA = 3
tentativas = 1

print(f'Você tem {MAX_TENTATIVA} para descobrir o número secreto.')
num_str = input(f'Informe a primeira tentativa: ')
num_user = int(num_str)
num_ok = num_user == NUM_SECRETO
if num_ok:
    print(f'Parabéns, você acertou com {tentativas} palpite!')
else:
    tentativas += 1
    print(f'Você tem {MAX_TENTATIVA - 1} para descobrir o número secreto.')
    num_str = input(f'Informe a segunda tentativa: ')
    num_user = int(num_str)
    num_ok = num_user == NUM_SECRETO
    if num_ok:
        print(f'Parabéns, você acertou com {tentativas} palpite!')
    else:
        tentativas += 1
        print(f'Você tem {MAX_TENTATIVA - 2} para descobrir o número secreto.')
        num_str = input(f'Informe a terceira tentativa: ')
        num_user = int(num_str)
        num_ok = num_user == NUM_SECRETO
        if num_ok:
            print(f'Parabéns, você acertou com {tentativas} palpite!')
        else:
            print('Fim do jogo tentativas esgotadas.')