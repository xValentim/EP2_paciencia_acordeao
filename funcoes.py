def cria_baralho():
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = []
    for i in range(13):
        baralho.append(valores[i] + '♠')
        baralho.append(valores[i] + '♥')
        baralho.append(valores[i] + '♦')
        baralho.append(valores[i] + '♣')
    print(baralho)
    return baralho

def extrai_naipe(carta):
    return carta[-1]

def extrai_valor(carta):
    return carta[0:len(carta) - 1]

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