import random
import numpy as np

# Função para calcular a distância euclidiana entre duas cidades
def distancia_euclidiana(cidade1, cidade2):
    return np.linalg.norm(np.array(cidade1) - np.array(cidade2))

# Função para criar uma matriz de feromônios inicializada com um valor pequeno
def criar_matriz_feromonios(num_cidades):
    return np.ones((num_cidades, num_cidades)) * 0.01

# Função para escolher o próximo destino com base em probabilidades
def escolher_destino(feromonios, visitados, cidade_atual, alpha, beta):
    nao_visitados = [i for i in range(len(feromonios)) if i not in visitados]
    probabilidades = []
    
    for cidade in nao_visitados:
        probabilidade = (feromonios[cidade_atual][cidade] ** alpha) * ((1.0 / distancia_euclidiana(cidades[cidade_atual], cidades[cidade])) ** beta)
        probabilidades.append((cidade, probabilidade))
    
    total_probabilidade = sum(prob[1] for prob in probabilidades)
    probabilidades = [(prob[0], prob[1] / total_probabilidade) for prob in probabilidades]
    
    escolha = random.choices(probabilidades, k=1)[0]
    return escolha[0]

# Função para atualizar os feromônios com base nas soluções encontradas
def atualizar_feromonios(feromonios, trilha, taxa_evaporacao, Q):
    for i in range(len(trilha) - 1):
        cidade_atual, proxima_cidade = trilha[i], trilha[i+1]
        feromonios[cidade_atual][proxima_cidade] = (1 - taxa_evaporacao) * feromonios[cidade_atual][proxima_cidade] + Q

# Função principal do algoritmo ACO
def aco(num_formigas, num_iteracoes, alpha, beta, taxa_evaporacao, Q):
    num_cidades = len(cidades)
    melhor_rota = None
    melhor_distancia = float('inf')
    feromonios = criar_matriz_feromonios(num_cidades)
    
    for _ in range(num_iteracoes):
        for formiga in range(num_formigas):
            cidade_atual = random.randint(0, num_cidades - 1)
            visitados = [cidade_atual]
            
            while len(visitados) < num_cidades:
                proxima_cidade = escolher_destino(feromonios, visitados, cidade_atual, alpha, beta)
                visitados.append(proxima_cidade)
                cidade_atual = proxima_cidade
            
            distancia_rota = sum(distancia_euclidiana(cidades[visitados[i]], cities[visitados[i+1]]) for i in range(num_cidades - 1))
            
            if distancia_rota < melhor_distancia:
                melhor_distancia = distancia_rota
                melhor_rota = visitados[:]
        
        atualizar_feromonios(feromonios, melhor_rota, taxa_evaporacao, Q)
    
    return melhor_rota, melhor_distancia

# Lista de coordenadas das cidades
cidades = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Parâmetros do ACO
num_formigas = 10
num_iteracoes = 100
alpha = 1.0
beta = 1.0
taxa_evaporacao = 0.5
Q = 1.0

# Executar o algoritmo ACO
melhor_rota, melhor_distancia = aco(num_formigas, num_iteracoes, alpha, beta, taxa_evaporacao, Q)

print("Melhor rota encontrada:", melhor_rota)
print("Melhor distância encontrada:", melhor_distancia)
