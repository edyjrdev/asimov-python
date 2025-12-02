li_num = list(range(1,21))


li_par = [e for e in li_num if e % 2 == 0]
li_impar = [e for e in li_num if e % 2 == 1]
li_raiz = [(e ** (1/2)) for e in li_num]
li_cubo_div_tres = [(e ** 3) for e in li_num if e % 3 == 0]

print(li_num)
print(li_par)
print(li_impar)
print(li_raiz)
print(li_cubo_div_tres)
