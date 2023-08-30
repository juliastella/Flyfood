import random


class Cidade:
    """ Inicia a cidade com duas coordenadas x,y"""
    def __init__(self, coordenadas):
        self.x = coordenadas[0]
        self.y = coordenadas[1]


class Individuo:
    def __init__(self, cidades):
        self.rota = random.sample(cidades, len(cidades))
        self.fitness = None


    def ifitness(self):
        """Calcula o fitness de cada individuo à partir da soma das distâncias euclidianas"""
        custo_total = 0
        percurso = self.rota

        for cidade in range(len(percurso)):
            if cidade < (len(percurso) -1):
                # Soma as distancias da primeira até a última cidade
                custo_total += distEuclidiana(percurso[cidade], percurso[cidade + 1])
            else:
                # Soma a distância da última cidade para a primeira.
                custo_total += distEuclidiana(percurso[cidade], percurso[0])
        self.fitness = 1 / custo_total


def distEuclidiana(cidade1, cidade2):
    """Calcula a distância entre as cidades com a fórmula de distância euclidiana"""
    return ((cidade2.x - cidade1.x)**2 + (cidade2.y - cidade1.y)**2) **0.5


def comparaAdd(lista, individuo):
    for objeto in lista:
        if objeto.rota == individuo.rota:
            return
    lista.append(individuo)


def popInicial(cidades ,tamanho_populacao):
    """Cria população inicial com quantidade x de indíviduos """
    populacao = []
    while len(populacao) != tamanho_populacao:
        individuo = Individuo(cidades)
        comparaAdd(populacao, individuo)
    return populacao


def fitPopulacao(populacao):
    """Calcula e armazena o fitness de toda a população"""
    for individuo in populacao:
        individuo.ifitness()


def torneio(populacao, tamanho_populacao):
    """ Seleção por Torneio"""
    pais = [0 for _ in tamanho_populacao]
    for torneio in range(tamanho_populacao):
        indice1 = random.randint(0, len(populacao) -1)
        indice2 = random.randint(0, len(populacao) -1)
        if populacao[indice1].fitness > populacao[indice2].fitness:
            pais[torneio] = populacao[indice1]
        else:
            pais[torneio] = populacao[indice2]
    return pais




# # Para testes...
# cidades = []
# c1 = [(1,0),(2,0),(3,1),(4,3),(5,4)]
# for i in c1:
#     cidades.append(Cidade(i))

# tamanho = 5

# i1 = Individuo(cidades)
# populacao =  popInicial(cidades, tamanho)
# fitPopulacao(populacao)