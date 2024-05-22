# numeros = [22, 44, 33, 21, 12, 11, 23, 37, 36, 46, 45, 41]

# for g in numeros:
#     if g % 2 == 0:
#         print(g)

numeros = [22, 44, 33, 21, 12, 11, 23, 37, -36, -46, 45, -41]
positivos = []
negativo = []

for g in numeros:
    if (g >= 0):
        positivos.append(g)
    else:
        negativo.append(g)
    
print ("Positivos:", positivos)
print ("Negativos:", negativo)

