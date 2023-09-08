import random
import matplotlib.pyplot as plt

class Formiga:
    def __init__(self, cidade_inicial, num_cidades):
        self.cidade_atual = cidade_inicial
        self.cidades_nao_visitadas = set(range(num_cidades))
        self.cidades_nao_visitadas.remove(cidade_inicial)
        self.rota = [cidade_inicial]

    def selecionar_proxima_cidade(self, feromonio, cidades, alfa, beta):
        probabilidade = [0] * len(self.cidades_nao_visitadas)
        total_probabilidade = 0

        for i, cidade in enumerate(self.cidades_nao_visitadas):
            if self.cidade_atual is not None and cidade is not None:
                probabilidade[i] = (feromonio[self.cidade_atual][cidade] ** alfa) * (1.0 / distEuclidiana(cidades[self.cidade_atual], cidades[cidade]) ** beta)
                total_probabilidade += probabilidade[i]
        
        if total_probabilidade == 0:
            return

        probabilidade = [p / total_probabilidade for p in probabilidade]
        escolha = random.uniform(0, 1)
        soma_probabilidade = 0

        cidades_nao_visitadas_list = list(self.cidades_nao_visitadas)  # Converta o conjunto em uma lista
        for i, p in enumerate(probabilidade):
            soma_probabilidade += p
            if escolha <= soma_probabilidade:
                proxima_cidade_index = i  # Índice selecionado aleatoriamente
                break

        proxima_cidade = cidades_nao_visitadas_list[proxima_cidade_index]  # Selecione a cidade apropriada da lista
        self.rota.append(proxima_cidade)
        self.cidade_atual = proxima_cidade
        cidades_nao_visitadas_list.remove(proxima_cidade)  # Remova a cidade da lista
        self.cidades_nao_visitadas = set(cidades_nao_visitadas_list)

def distEuclidiana(cidade1, cidade2):
    return ((cidade2[0] - cidade1[0]) ** 2 + (cidade2[1] - cidade1[1]) ** 2) ** 0.5

def calcular_distancia_rota(rota, cidades):
    distancia_total = 0
    for i in range(len(rota)):
        cidade_atual = cidades[rota[i]]
        cidade_seguinte = cidades[rota[(i + 1) % len(rota)]]
        distancia_total += distEuclidiana(cidade_atual, cidade_seguinte)
    return distancia_total

def construir_trilha(cidades, num_formigas, num_geracoes, alfa=1.0, beta=1.0, taxa_evaporacao=0.1):
    num_cidades = len(cidades)
    melhor_rota = None
    melhor_distancia = float('inf')
    feromonio = [[1.0 for _ in range(num_cidades)] for _ in range(num_cidades)]

    for _ in range(num_geracoes):
        for _ in range(num_formigas):
            cidade_inicial = random.randint(0, num_cidades - 1)
            formiga = Formiga(cidade_inicial, num_cidades)

            while formiga.cidades_nao_visitadas:
                formiga.selecionar_proxima_cidade(feromonio, cidades, alfa, beta)

            distancia_total = calcular_distancia_rota(formiga.rota, cidades)

            if distancia_total < melhor_distancia:
                melhor_rota = formiga.rota[:]
                melhor_distancia = distancia_total

            for i in range(num_cidades):
                for j in range(i+1, num_cidades):
                    feromonio[i][j] *= (1.0 - taxa_evaporacao)
                    feromonio[j][i] = feromonio[i][j]
                for cidade in formiga.rota:
                    if cidade != cidade_inicial:
                        quantidade_depositada = 1.0 / distancia_total
                        feromonio[cidade_inicial][cidade] += quantidade_depositada
                        feromonio[cidade][cidade_inicial] = feromonio[cidade_inicial][cidade]

    return melhor_rota, melhor_distancia

def main():
    coords = [(64, 96), (80, 39), (69, 23), (72, 42)]

    num_formigas = 50
    num_geracoes = 500
    alfa = 1.0
    beta = 1.0
    taxa_evaporacao = 0.1

    melhor_rota, melhor_distancia = construir_trilha(coords, num_formigas, num_geracoes, alfa, beta, taxa_evaporacao)

    print(f"Melhor rota encontrada: {melhor_rota}")
    print(f"Melhor distância encontrada: {melhor_distancia}")

    x = [coords[i][0] for i in melhor_rota]
    y = [coords[i][1] for i in melhor_rota]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, marker='o')
    plt.show()

if __name__ == "__main__":
    main()
