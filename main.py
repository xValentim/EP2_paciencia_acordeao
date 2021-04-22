from funcoes import *
with open('inicio.txt', encoding='utf-8') as f:
    data = f.read()
print(data)

continua = False
while continua != True:
    iniciar = input("Deseja iniciar? (Digite s ou n) ... ")
    if iniciar == 's':
        continua = True

# Pula uma linha
print('\n')

# Gera baralho
baralho = cria_baralho()
estado_baralho(baralho)