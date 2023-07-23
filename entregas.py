def permutar(pontos_de_entrega):
    if len(pontos_de_entrega) <= 1:
        return [pontos_de_entrega]

    return [[ponto_atual] + permutacao
            for i, ponto_atual in enumerate(pontos_de_entrega)
            for permutacao in permutar(pontos_de_entrega[:i] + pontos_de_entrega[i+1:])]

def ler_matriz(nome_arquivo, lista_pontos, coordenadas, lista_r):
  with open(nome_arquivo, 'r') as arquivo:
    n, m = [int(i) for i in arquivo.readline().split()]
    matriz = [list(linha.split()) for linha in arquivo]

# Armazenar cada ponto da matriz em uma lista

  for linha in range(n):
    for coluna in range(m):
        if matriz[linha][coluna] != '0':
            if (matriz[linha][coluna] == 'R'):
             lista_r.append([linha, coluna])
            else:
              lista_pontos.append(matriz[linha][coluna])
              coordenadas.append([linha, coluna])

  return n, m, lista_r
     
pontos_de_entrega = []
pontos_da_coodernada = []
lista_r = []

linhas, colunas = ler_matriz('matriz.txt', pontos_de_entrega, pontos_da_coodernada, lista_r)

print(pontos_de_entrega)

# print(permutar(pontos_de_entrega))











# lista_p = []
# coordenadasA = []

# linha, coluna = ler_matriz('matriz.txt', lista_p, coordenadasA)

# print(lista_p)
# print(coordenadasA)
# print(linha, coluna)