arquivo = open('matriz', 'r')

print(arquivo)

n, m = arquivo.readline().split() # pega o arquivo e divide em linhas e colunas n e m
linhas = arquivo.read().splitlines()

coordenadas = {}
pontoDeliver = []

print(coordenadas, pontoDeliver)