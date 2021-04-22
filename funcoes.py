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