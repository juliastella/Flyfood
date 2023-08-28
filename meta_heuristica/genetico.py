import matplotlib
import random


class Cidade:
    """ Inicia a cidade com duas coordenadas x,y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y



def distanciaEuc(c1, c2):
    """Usa a formula da distância euclidiana para calcular a distância entre duas cidades"""
    return ((c2.x - c1.x)**2 + (c2.y - c1.y)**2) **0.5


def popInicial(tam_pop, cidades):
    """ Cria a população inicial de tamanho tam_pop com permutações da lista 'cidades'. """
    populacao = []

    while len(populacao) != tam_pop:
        rota = random.sample(cidades, len(cidades))
        if rota not in populacao:
            populacao.append(rota)
    return populacao


