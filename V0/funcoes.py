import random

# Tabela de cores - Usadas pela função "colorir"
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
YELLOW  = "\033[1;33m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

# Funçao que cria baralho e embaralha as cartasS (shuffle)
def cria_baralho():
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['♠', '♥', '♦', '♣']
    baralho = [valor + naipe for valor in valores for naipe in naipes]
    random.shuffle(baralho)
    return baralho

# Extrai o naipe da carta (ultima posição da string)
def extrai_naipe(carta):
    return carta[-1]

# Extrai valor da carta (todas as posições, exceto a ultima)
def extrai_valor(carta):
    return carta[0:len(carta) - 1]

# Função usada para colorir as cartas
def colorir(carta):
    if extrai_naipe(carta) == '♠':
        carta = BLUE + carta + RESET
    elif extrai_naipe(carta) == '♥':
        carta = RED + carta + RESET
    elif extrai_naipe(carta) == '♦':
        carta = YELLOW + carta + RESET
    elif extrai_naipe(carta) == '♣':
        carta = GREEN + carta + RESET
    return carta

# Mostra o estado das cartas no baralho
def estado_baralho(baralho):
    print('O estado atual do baralho é:\n')
    for i in range(len(baralho)):
        print(str(i + 1) + '.  ' + colorir(baralho[i]))

# Lista os movimentos possíveis
def lista_movimentos_possiveis(baralho, posicao):
    movimentos = []
    carta = baralho[posicao]
    naipe = extrai_naipe(carta)
    valor = extrai_valor(carta)
    
    if posicao >= 3:
        carta_1 = baralho[posicao - 1]
        naipe_1 = extrai_naipe(carta_1)
        valor_1 = extrai_valor(carta_1)
        if naipe == naipe_1 or valor == valor_1:
            movimentos.append(1)
        carta_3 = baralho[posicao - 3]
        naipe_3 = extrai_naipe(carta_3)
        valor_3 = extrai_valor(carta_3)
        if naipe == naipe_3 or valor == valor_3:
            movimentos.append(3)
            
    elif posicao >= 1:
        carta_1 = baralho[posicao - 1]
        naipe_1 = extrai_naipe(carta_1)
        valor_1 = extrai_valor(carta_1)
        if naipe == naipe_1 or valor == valor_1:
            movimentos.append(1)
    return movimentos

# Movimento de empilhar cartas
def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

# Verifica se tem movimentos possíveis
def possui_movimentos_possiveis(baralho):
    for i in range(len(baralho)):
        movimentos = lista_movimentos_possiveis(baralho, i)
        if movimentos != []:
            return True
    return False