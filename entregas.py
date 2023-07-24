import time


def add_r(lista, R):
    for j in lista:
        j.append(R)
        j.insert(0, R)
    return lista

def permutar(pontos_de_entrega):

    if len(pontos_de_entrega) <= 1:
        return [pontos_de_entrega]

    return [[ponto_atual] + permutacao
            for i, ponto_atual in enumerate(pontos_de_entrega)
            for permutacao in permutar(pontos_de_entrega[:i] + pontos_de_entrega[i+1:])]



def dist_percurso( percurso):
    distancia_total = 0
    d = 0
    for i in range(1,len(percurso)):
        p1 = percurso[i - 1]
        p2 = percurso[i]
        d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        distancia_total += d
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
              coordenada = (linha, coluna)
              coordenadas.append(coordenada)

  return coordenadas_R, matriz



def main():
    tic = time.process_time()
    # Recebe as letras
    pontos_de_entrega = []
    # Recebe as tuplas
    pontos_da_coodernada = []

    ponto_R, matriz_teste = ler_matriz('matriz.txt', pontos_de_entrega, pontos_da_coodernada)
    #Recebe lista de permutações    
    permutados = permutar(pontos_da_coodernada)



    # Cálculo distância
    menor_dist = float('inf')
    menor_percurso = None
    for caminho in add_r(permutados, ponto_R):
        dist = dist_percurso(caminho)
        if dist < menor_dist:
            menor_dist = dist
            menor_percurso = caminho

    # De acordo com as coordenadas, chama os pontos da permutação
    for i in menor_percurso:
        print(f'{matriz_teste[i[0]][i[1]]}',end=' ')
    print(f'\nMenor distância: {menor_dist}')


    # Calcula o tempo
    toc = time.process_time()
    tempo_de_execucao = toc - tic
    print(f'O tempo de execução é: {tempo_de_execucao}s')
    

main()