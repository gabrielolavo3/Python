# x = 'Gabriel'
# y = 14
# z = 2.3
# w = True

# Operadores matemáticos

n1 = 4.5
n2 = 6.3
n3 = 5.4

media = (n1 + n2 + n3) / 3

# Estrutura condicional

if (media >= 7):
    situacao = 'aprovado'

elif (media >= 3 and media < 7):
    situacao = 'para recuperação'

else:
    situacao = 'reprovado'

# print(media)
print (f'A sua média foi {media:.1f}, você foi {situacao}')