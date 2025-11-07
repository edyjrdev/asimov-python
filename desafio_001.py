# Desafio 001

#configuracao
user_bd = 'edyjr'
senha_bd = 'topsecret'

#entrada
user = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')


# processamento
user_ok = user == user_bd
senha_ok = senha == senha_bd

# saida
if not user_ok:
    print(f'Usuário incorreto.')
else:
    if not senha_ok:
        print(f'Senha incorreta.')

if user_ok and senha_ok:
    print(f'Olá, {user} bem vindo!')