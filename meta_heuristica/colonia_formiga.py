import random
import matplotlib.pyplot as plt
import time

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

def construir_trilha(cidades, num_formigas, num_geracoes, alfa=1.0, beta=1.0, taxa_evaporacao=0.1, num_elites=1):
    num_cidades = len(cidades)
    feromonio = [[1.0 for _ in range(num_cidades)] for _ in range(num_cidades)]
    
    melhor_rota_global = None
    melhor_distancia_global = float('inf')
    melhor_distancia_por_geracao = []

    geracoes_sem_melhoria = 0
    elites = []

    for geracao in range(num_geracoes):
        melhor_rota_local = None
        melhor_distancia_local = float('inf')
        
        for _ in range(num_formigas):
            cidade_inicial = random.randint(0, num_cidades - 1)
            formiga = Formiga(cidade_inicial, num_cidades)

            while formiga.cidades_nao_visitadas:
                formiga.selecionar_proxima_cidade(feromonio, cidades, alfa, beta)

            distancia_total = calcular_distancia_rota(formiga.rota, cidades)

            if distancia_total < melhor_distancia_local:
                melhor_rota_local = formiga.rota[:]
                melhor_distancia_local = distancia_total

        # Atualize o melhor resultado global se necessário
        if melhor_distancia_local < melhor_distancia_global:
            melhor_rota_global = melhor_rota_local[:]
            melhor_distancia_global = melhor_distancia_local
            geracoes_sem_melhoria = 0
        else:
            geracoes_sem_melhoria += 1

        melhor_distancia_por_geracao.append(melhor_distancia_global)

        print(f"Geração {geracao + 1}, Melhor fitness local: {1.0 / melhor_distancia_local}")

        # Adicione as elites à lista
        if len(elites) < num_elites or melhor_distancia_local < min(elites):
            elites.append(melhor_distancia_local)

        # Atualize o feromônio apenas das elites
        for i in range(num_cidades):
            for j in range(i + 1, num_cidades):
                if melhor_distancia_local in elites:
                    feromonio[i][j] *= (1.0 - taxa_evaporacao)
                    feromonio[j][i] = feromonio[i][j]
                for cidade in melhor_rota_local:
                    if cidade != cidade_inicial:
                        quantidade_depositada = 1.0 / melhor_distancia_local
                        feromonio[cidade_inicial][cidade] += quantidade_depositada
                        feromonio[cidade][cidade_inicial] = feromonio[cidade_inicial][cidade]
        
    return melhor_rota_global, melhor_distancia_global, melhor_distancia_por_geracao

def lerCoordenadas(arquivo):
    coordenadas = []
    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            x = float(partes[1])
            y = float(partes[2])
            coordenadas.append((x, y))
    return coordenadas

def main():
    coordenadas = lerCoordenadas('/home/me/Documents/Faculdade/periodo-02/Flyfood/meta_heuristica/berlin52.txt')

    num_formigas = 50
    num_geracoes = 500
    alfa = 1.0
    beta = 1.0
    taxa_evaporacao = 0.1

    start_time = time.time() 

    melhor_rota, melhor_distancia, melhor_distancia_por_geracao = construir_trilha(coordenadas, num_formigas, num_geracoes, alfa, beta, taxa_evaporacao)

    end_time = time.time() 

    tempo_de_execucao = end_time - start_time

    print(f"Melhor rota encontrada: {melhor_rota}")
    print(f"Melhor distância encontrada: {melhor_distancia}")
    print(f"Tempo de execução: {tempo_de_execucao} segundos\n")

    x = [coordenadas[i][0] for i in melhor_rota]
    y = [coordenadas[i][1] for i in melhor_rota]

    plt.figure(figsize=(12, 6))
    
    # Gráfico 1: Melhor rota encontrada
    plt.subplot(1, 2, 1)
    plt.plot(x, y, marker='o')
    plt.title('Melhor Rota Encontrada')
    
    # Gráfico 2: Evolução da Melhor Distância
    plt.subplot(1, 2, 2)
    plt.plot(melhor_distancia_por_geracao, marker='o')
    plt.title('Evolução da Melhor Distância')
    plt.xlabel('Geração')
    plt.ylabel('Distância')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()