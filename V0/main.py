from funcoes import *
with open('V0/inicio.txt', encoding='utf-8') as f:
    data = f.read()
print(data)

continua = False
while continua != True:
    iniciar = input("Deseja iniciar? (Digite s ou n) ... ")
    if iniciar == 's':
        continua = True

# Pula uma linha
print('\n')

while continua:

    # Gera baralho
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho):

        # Mostra todo o baralho
        estado_baralho(baralho)

        # Pula uma linha
        print('\n')
        indice_carta = int(input(f"Escolha uma carta (digite um número entre 1 e {len(baralho)}):  "))
        aux_i = indice_carta - 1
        escolhendo_carta = True
        while escolhendo_carta:

            # Trocar por try e except
            # Verifica se a carta é válida
            if indice_carta > len(baralho):
                carta_valida = False
                while carta_valida != True:
                    indice_carta = int(input(f"Posição inválida. Por favor, digite um número entre 1 e {len(baralho)}):"))
                    if indice_carta > 0 and indice_carta <= len(baralho):
                        carta_valida = True
                        aux_i = indice_carta - 1

            # Verifica movimentos possiveis
            movimentos = lista_movimentos_possiveis(baralho, aux_i)    
            if len(movimentos) == 0:
                indice_carta = int(input(f'A carta {baralho[aux_i]} não pode ser movida. Por favor, digite um número entre 1 e {len(baralho)}):  '))
                aux_i = indice_carta - 1
            elif len(movimentos) == 1:
                origem = aux_i
                destino = origem - movimentos[0]
                baralho = empilha(baralho, origem, destino)
                escolhendo_carta = False
            else:
                #Dois movimentos possiveis
                print(f"Sobre qual carta você quer empilhar o {baralho[aux_i]}? \n 1. {baralho[aux_i - 1]} \n 2. {baralho[aux_i - 3]} \n")
                choice = int(input("Digite o número de sua escolha (1 ou 2): "))

                # Pergunta ao usuário onde ele quer empilhar
                escolhendo_onde_empilhar = True
                while escolhendo_onde_empilhar:
                    if choice == 1:
                        origem = aux_i
                        destino = origem - 1
                        baralho = empilha(baralho, origem, destino)
                        escolhendo_onde_empilhar = False
                        escolhendo_carta = False
                    elif choice == 2:
                        origem = aux_i
                        destino = origem - 3
                        baralho = empilha(baralho, origem, destino)
                        escolhendo_onde_empilhar = False
                        escolhendo_carta = False
                    else:
                        print(f"Opção inválida. Sobre qual carta você quer empilhar o {baralho[aux_i]}? \n 1. {baralho[aux_i - 1]} \n 2. {baralho[aux_i - 3]} \n")
                        choice = int(input("Digite o número de sua escolha (1 ou 2): "))

    if len(baralho) > 1:
        print('Você perdeu :( ')
    else:
        print('Você ganhou :) ')
    
    resposta = input("Você quer jogar novamente (digite s ou n)? ")
    if resposta == 'n':
        continua = False
