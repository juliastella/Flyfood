def permutar(pontos_de_entrega):
    if len(pontos_de_entrega) <= 1:
        return [pontos_de_entrega]

    return [[ponto_atual] + permutacao
            for i, ponto_atual in enumerate(pontos_de_entrega)
            for permutacao in permutar(pontos_de_entrega[:i] + pontos_de_entrega[i+1:])]

def distancia(p1, p2):
    distancia = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    return distancia

def dist_percurso( percurso):
    distancia_total = 0
    for i in range(1,len(percurso)):
        distancia_total += distancia(percurso[i-1],percurso[i])
    return distancia_total


def ler_matriz(nome_arquivo, lista_pontos, coordenadas):
  with open(nome_arquivo, 'r') as arquivo:
    n, m = [int(i) for i in arquivo.readline().split()]
    matriz = [list(linha.split()) for linha in arquivo]

# Armazenar cada ponto da matriz em uma lista

  for linha in range(n):
    for coluna in range(m):
        if matriz[linha][coluna] != '0':
            if (matriz[linha][coluna] == 'R'):
              coordenadas_R = (linha, coluna)
            else:
              lista_pontos.append(matriz[linha][coluna])
              coordenadas.append([linha, coluna])

  return n, m, coordenadas_R
     
pontos_de_entrega = []
pontos_da_coodernada = []

linhas, colunas, ponto_R = ler_matriz('matriz.txt', pontos_de_entrega, pontos_da_coodernada)


for j in permutar(pontos_da_coodernada):
   pontos_da_coodernada.append(ponto_R)
   pontos_da_coodernada.insert(0,ponto_R)
   print(pontos_da_coodernada)











# lista_p = []
# coordenadasA = []

# linha, coluna = ler_matriz('matriz.txt', lista_p, coordenadasA)

# print(lista_p)
# print(coordenadasA)
# print(linha, coluna)