import random
from matplotlib import pyplot as plt

def distEuclidiana(cidade1, cidade2):
    return ((cidade2["x"] - cidade1["x"]) ** 2 + (cidade2["y"] - cidade1["y"]) ** 2) ** 0.5

def calcular_distancia_rota(rota):
    distancia_total = 0
    for i in range(len(rota)):
        cidade_atual = rota[i]
        cidade_seguinte = rota[(i + 1) % len(rota)]  # Loop de volta à primeira cidade
        distancia_total += distEuclidiana(cidade_atual, cidade_seguinte)
    return distancia_total

def criar_trilha_aleatoria(cidades):
    return random.sample(cidades, len(cidades))

def atualizar_feromonio(feromonio, rota, distancia_total, taxa_evaporacao):
    feromonio_depositado = 1.0 / distancia_total
    for i in range(len(rota)):
        cidade_atual = rota[i]
        cidade_seguinte = rota[(i + 1) % len(rota)]  # Loop de volta à primeira cidade
        feromonio[cidade_atual]["feromonio"] *= (1.0 - taxa_evaporacao)  # Evaporação
        feromonio[cidade_atual]["feromonio"] += feromonio_depositado
        feromonio[cidade_seguinte]["feromonio"] *= (1.0 - taxa_evaporacao)  # Evaporação
        feromonio[cidade_seguinte]["feromonio"] += feromonio_depositado

def selecionar_proxima_cidade(cidade_atual, cidades_nao_visitadas, feromonio, alfa=1.0, beta=1.0):
    probabilidade = [0] * len(cidades_nao_visitadas)
    total_probabilidade = 0

    for i, cidade in enumerate(cidades_nao_visitadas):
        probabilidade[i] = (feromonio[cidade_atual]["feromonio"] ** alfa) * (1.0 / distEuclidiana(cidade_atual, cidade)) ** beta
        total_probabilidade += probabilidade[i]

    probabilidade = [p / total_probabilidade for p in probabilidade]
    escolha = random.uniform(0, 1)
    soma_probabilidade = 0

    for i, p in enumerate(probabilidade):
        soma_probabilidade += p
        if escolha <= soma_probabilidade:
            return cidades_nao_visitadas[i]

def construir_trilha(cidades, num_formigas, num_geracoes, alfa=1.0, beta=1.0, taxa_evaporacao=0.1):
    melhor_rota = None
    melhor_distancia = float('inf')
    feromonio = [{"x": cidade["x"], "y": cidade["y"], "feromonio": 1.0} for cidade in cidades]

    for _ in range(num_geracoes):
        for _ in range(num_formigas):
            cidade_inicial = random.choice(cidades)
            cidades_nao_visitadas = list(cidades)
            cidades_nao_visitadas.remove(cidade_inicial)
            rota = [cidade_inicial]

            while cidades_nao_visitadas:
                proxima_cidade = selecionar_proxima_cidade(rota[-1], cidades_nao_visitadas, feromonio, alfa, beta)
                rota.append(proxima_cidade)
                cidades_nao_visitadas.remove(proxima_cidade)

            distancia_total = calcular_distancia_rota(rota)

            if distancia_total < melhor_distancia:
                melhor_rota = rota
                melhor_distancia = distancia_total

            atualizar_feromonio(feromonio, rota, distancia_total, taxa_evaporacao)

    return melhor_rota, melhor_distancia

def main():
    coords = [(64, 96), (80, 39), (69, 23), (72, 42), (48, 67), (58, 43), (81, 34), (79, 17), (30, 23), (42, 67), (7, 76),
             (29, 51), (78, 92), (64, 8), (95, 57), (57, 91), (40, 35), (68, 40), (92, 34), (62, 1), (28, 43), (76, 73),
             (67, 88), (93, 54), (6, 8), (87, 18), (30, 9), (77, 13), (78, 94), (55, 3), (82, 88), (73, 28), (20, 55),
             (27, 43), (95, 86), (67, 99), (48, 83), (75, 81), (8, 19), (20, 18), (54, 38), (63, 36), (44, 33), (52, 18),
             (12, 13), (25, 5), (58, 85), (5, 67), (90, 9), (41, 76), (25, 76), (37, 64), (56, 63), (10, 55), (98, 7),
             (16, 74), (89, 60), (48, 82), (81, 76), (29, 60), (17, 22), (5, 45), (79, 70), (9, 100), (17, 82), (74, 67),
             (10, 68), (48, 19), (83, 86), (84, 94)]

    num_formigas = 50
    num_geracoes = 500
    alfa = 1.0
    beta = 1.0
    taxa_evaporacao = 0.1  # Taxa de evaporação do feromônio

    cidades = [{"x": x, "y": y} for x, y in coords]

    melhor_rota, melhor_distancia = construir_trilha(cidades, num_formigas, num_geracoes, alfa, beta, taxa_evaporacao)

    print(f"Melhor rota encontrada: {melhor_rota}")
    print(f"Melhor distância encontrada: {melhor_distancia}")

    # Se desejar, pode plotar o gráfico da melhor rota
    x = [cidade["x"] for cidade in melhor_rota]
    y = [cidade["y"] for cidade in melhor_rota]
    x.append(x[0])  # Para fechar o ciclo
    y.append(y[0])  # Para fechar o ciclo
    plt.plot(x, y, marker='o')
    plt.show()

if __name__ == "__main__":
    main()
