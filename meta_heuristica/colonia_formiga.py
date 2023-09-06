import random
import math

# Defina os pontos de entrega no plano cartesiano
pontos_entrega = {
    'A': (1, 1),
    'B': (3, 2),
    'C': (2, 4),
    'D': (0, 4)
}

# Parâmetros do algoritmo de colônia de formigas
num_formigas = 100       # Número de formigas
num_iteracoes = 100      # Número de iterações
alpha = 1.0              # Peso do feromônio
beta = 2.0               # Peso da distância
taxa_evaporacao = 0.1    # Taxa de evaporção do feromônio

# Função para calcular a distância euclidiana entre dois pontos
def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Inicialização das trilhas de feromônio
feromonio = {}
for ponto1 in pontos_entrega:
    for ponto2 in pontos_entrega:
        feromonio[(ponto1, ponto2)] = 1.0

# Função para calcular a probabilidade de escolher o próximo ponto
def calcular_probabilidade(ponto_atual, ponto_destino, visitados):
    probabilidade = 0.0
    for ponto in pontos_entrega:
        if ponto not in visitados:
            probabilidade += (feromonio[(ponto_atual, ponto)] ** alpha) * ((1.0 / calcular_distancia(pontos_entrega[ponto_atual], pontos_entrega[ponto])) ** beta)
    return probabilidade

# Função para escolher o próximo ponto com base nas probabilidades
def escolher_proximo_ponto(ponto_atual, visitados):
    probabilidades = {}
    for ponto in pontos_entrega:
        if ponto not in visitados:
            probabilidade = calcular_probabilidade(ponto_atual, ponto, visitados)
            probabilidades[ponto] = probabilidade

    total_probabilidade = sum(probabilidades.values())
    r = random.uniform(0, total_probabilidade)
    acumulado = 0.0

    for ponto, prob in probabilidades.items():
        acumulado += prob
        if acumulado >= r:
            return ponto

# Função para atualizar as trilhas de feromônio
def atualizar_feromonio(caminhos, melhor_caminho):
    for ponto1, ponto2 in caminhos:
        feromonio[(ponto1, ponto2)] *= (1.0 - taxa_evaporacao)
    for ponto1, ponto2 in melhor_caminho:
        feromonio[(ponto1, ponto2)] += 1.0 / melhor_custo_global

# Algoritmo de colônia de formigas
melhor_caminho_global = None
melhor_custo_global = float('inf')

for _ in range(num_iteracoes):
    for _ in range(num_formigas):
        ponto_atual = 'A'      # Inicializa em um dos pontos de entrega
        visitados = [ponto_atual]         # Lista de pontos visitados
        caminho = []           # Caminho percorrido pela formiga

        while len(visitados) < len(pontos_entrega):
            proximo_ponto = escolher_proximo_ponto(ponto_atual, visitados)
            caminho.append((ponto_atual, proximo_ponto))
            visitados.append(proximo_ponto)
            ponto_atual = proximo_ponto

        atualizar_feromonio(caminho, caminho)
        
        custo_caminho = sum([calcular_distancia(pontos_entrega[p1], pontos_entrega[p2]) for p1, p2 in caminho])

        if custo_caminho < melhor_custo_global:
            melhor_caminho_global = caminho
            melhor_custo_global = custo_caminho

# Resultados
print("Melhor rota encontrada:", [p[0] for p in melhor_caminho_global])
print("Menor custo:", melhor_custo_global)
