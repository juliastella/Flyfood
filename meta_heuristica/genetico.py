import random


class Cidade:
    """ Inicia a cidade com duas coordenadas x,y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distEuclidiana(self, cidade2):
        """Calcula a distância entre as cidades com a fórmula de distância euclidiana"""
        return ((cidade2.x - self.x)**2 + (cidade2.y - self.y)**2) **0.5


class Populacao:
    pass



def popInicial(tamanho_populacao, cidades):
    """Cria população inicial com quantidade 'tam_pop' de indíviduos """
    populacao = []
    while len(populacao) != tamanho_populacao:
        rota = random.sample(cidades, len(cidades))
        if rota not in populacao:
            populacao.append(rota)
    return populacao


def fitIndividuo(individuo):
    """Calcula o fitness de cada individuo à partir da soma das distâncias euclidianas"""
    custo_total = 0
    for cidade in range(len(individuo)):
        if cidade < (len(individuo) -1):
            # Soma as distancias da primeira até a última cidade
            custo_total += cidade.distEuclidiana(cidade + 1)
        else:
            # Soma a distância da última cidade para a primeira.
            custo_total += cidade.distEuclidiana(individuo[0])
    return 1 / custo_total


def fitPopulacao(populacao, tamanho_populacao):
    """Calcula e armazena o fitness de toda a população"""
    fitness = [0 for _ in range(tamanho_populacao)]
    for indice, individuo in enumerate(populacao):
        fitness[indice] = fitIndividuo(individuo)
    return fitness
    
def torneio(populacao, fitness, tamanho_populacao):
    """ Seleção por Torneio"""
    pass

