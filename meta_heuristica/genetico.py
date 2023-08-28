import numpy as random, matplotlib
from typing import List, Tuple

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


def avaliar_rota(rota: List[str], coordenadas: List[tuple[int, int]]) -> float:
    """ Primeira parte do fitness, calcula todas as coodernadas e retona o custo de cada uma."""
    custo_total = 0
    ponto_anterior = 'R' # Ponto de origem.
    coordenadas_dicionario = {coordenadas} # Converto a minha lista em um dicionario, para o acesso mais rapido

    for ponto_atual in rota: # calculo da distancia de todos os pontos das coordenadas
      if ponto_atual != ponto_anterior:
          custo_total += distanciaEuc(coordenadas_dicionario[ponto_anterior], coordenadas_dicionario[ponto_atual])
    
    return custo_total

def avaliar_populacao(populacao: List[str], coordenadas: List[tuple[int, int]]) -> list[float]:
    """Ultima parte do fitness: calcula os valores de fitness para cada rota na população e armazena elas em uma lista"""


    fitnes = []

    for rota in populacao:
        custo_rota = avaliar_rota(rota, coordenadas)
        fitnes.append(custo_rota)
    
    return fitnes
