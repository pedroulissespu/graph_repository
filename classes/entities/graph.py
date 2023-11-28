import collections
import math
import heapq
import sys
import operator

# Aumenta o limite de recursão do Python para evitar erros em grafos grandes
sys.setrecursionlimit(1000000000)

class Graph:
    def __init__(self, pathFile=str):
        # Inicializa a lista de adjacência do grafo
        self.listaAdjacencia = {}
        # Lê os dados do arquivo
        self.DataReader(pathFile)

    def add_edge(self, u, v, w):      
        # Adiciona uma aresta ao grafo. Se o vértice já existir na lista de adjacência, adiciona o vizinho à lista desse vértice. Caso contrário, cria uma nova entrada na lista de adjacência.
        if u in self.listaAdjacencia.keys():
            self.listaAdjacencia[u].append((v, w))
        else:
            self.listaAdjacencia.update({u: [(v, w)]})

        # Faz o mesmo para o vértice v, garantindo que a aresta seja adicionada em ambas as direções (grafo não direcionado)
        if v in self.listaAdjacencia.keys():
                self.listaAdjacencia[v].append((u, w))
        else:
            self.listaAdjacencia.update({v: [(u, w)]})

    def n(self):
        # Retorna o número de vértices no grafo
        return len(self.listaAdjacencia.keys())

    def m(self):
        # Retorna o número de arestas no grafo
        edges = 0
        
        for vertice, neighbors in self.listaAdjacencia.items():
            edges += len(neighbors)
        
        return edges // 2

    def viz(self, v):
        # Retorna a lista de vizinhos de um vértice
        if v in self.listaAdjacencia:
            return self.listaAdjacencia[v]
        else:
            return []

    def d(self, v):
        # Retorna o grau de um vértice (número de vizinhos)
        return len(self.viz(v))

    def w(self, uv):
        # Retorna o peso de uma aresta
        u, v = uv
        for vertex, weight in self.vertices[u]:
            if vertex == v:
                return weight
        return None

    def mind(self):
        # Retorna o menor grau entre todos os vértices do grafo
        return min([self.d(vertex) for vertex in self.listaAdjacencia.keys()]) // 2

    def maxd(self):
        # Retorna o maior grau entre todos os vértices do grafo
        return max([self.d(vertex) for vertex in self.listaAdjacencia.keys()]) // 2

    def bfs(self, v):
        # Realiza uma busca em largura a partir de um vértice v, retornando a distância e o predecessor de cada vértice
        d = {v: 0}
        pi = {v: None}
        queue = collections.deque([v])
        while queue:
            u = queue.popleft()
            for vertex, weight in self.vertices[u]:
                if vertex not in d:
                    d[vertex] = d[u] + 1
                    pi[vertex] = u
                    queue.append(vertex)
        return d, pi
    
    def dfs(self, v):
        # Realiza uma busca em profundidade a partir de um vértice v, retornando o predecessor e os tempos de início e fim de cada vértice
        visitado = {i: False for i in self.listaAdjacencia}
        tempo_inicio = {i: float('inf') for i in self.listaAdjacencia}
        tempo_fim = {i: float('inf') for i in self.listaAdjacencia}
        predecessor = {i: None for i in self.listaAdjacencia}
        tempo = [0]

        def dfs_visit(u):
            tempo[0] += 1
            tempo_inicio[u] = tempo[0]
            visitado[u] = True
            for vizinho, _ in self.listaAdjacencia[u]:
                if not visitado[vizinho]:
                    predecessor[vizinho] = u
                    dfs_visit(vizinho)
            tempo[0] += 1
            tempo_fim[u] = tempo[0]

        dfs_visit(v)
        return predecessor, tempo_inicio, tempo_fim

    def encontre_caminho(self, v, T):
        # Encontra um caminho de comprimento T a partir de um vértice v usando busca em profundidade
        visitado = {i: False for i in self.listaAdjacencia}
        caminho = []

        def dfs(v):
            visitado[v] = True
            caminho.append(v)

            if len(caminho) >= T:
                return True

            for vizinho, _ in self.listaAdjacencia[v]:
                if not visitado[vizinho] and dfs(vizinho):
                    return True

            caminho.pop()
            return False

        if dfs(v):
            return caminho
        else:
            return None

    def encontre_ciclos(self, v):
        # Encontra um ciclo de comprimento 50 a partir de um vértice v
        ciclos = self.encontre_caminho(v ,50)
        
        ciclosReverse = ciclos.copy()
        ciclosReverse.reverse()
        
        for vertice in ciclos:
            vizinhos = self.viz(vertice)
            for vizinho,_ in vizinhos:
                if ciclosReverse[0] == vizinho:
                    index = ciclos.index(vertice)
                    if index >= 5:
                        ciclo = ciclosReverse[0:index]
                        ciclo.append(ciclosReverse[0])
                        return ciclo

    def bf(self, v):
        # Implementa o algoritmo de Bellman-Ford para encontrar o caminho mais curto a partir de um vértice v
        d = {u: math.inf for u in self.vertices}
        d[v] = 0
        pi = {u: None for u in self.vertices}

        for _ in range(self.n() - 1):
            for u, v, w in self.edges:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    pi[v] = u

        for u, v, w in self.edges:
            if d[u] + w < d[v]:
                raise ValueError("Graph contains a negative-weight cycle")

        return d, pi

    def dijkstra(self, v):
        # Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto a partir de um vértice v
        d, antecessor, Q, visitado = {}, {}, [], set()

        [d.update({vert: 1000000000})for vert in self.listaAdjacencia.keys()]
        [antecessor.update({vert: None})
         for vert in self.listaAdjacencia.keys()]

        d[v] = 0

        heapq.heappush(Q, v)

        while Q:
            vert = heapq.heappop(Q)  # B

            if vert in visitado:
                continue
            visitado.add(vert)

            self.relaxaDijkstra(d, antecessor, vert)
            vizinhos = self.viz(vert)
            for vizinho, _ in vizinhos:
                if vizinho in visitado or vizinho in Q:
                    continue
                heapq.heappush(Q, vizinho)

        return d, antecessor

    def relaxaDijkstra(self, d, antecessor, vertice):
        # Função auxiliar para o algoritmo de Dijkstra que relaxa as arestas
        vizinhos = self.viz(vertice)
        for vizinho, peso in vizinhos:
            if d[vizinho] > d[vertice] + peso:
                d[vizinho] = d[vertice] + peso
                antecessor[vizinho] = vertice

    def distance(self, v):
        # Retorna o vértice mais distante a partir de um vértice v usando o algoritmo de Dijkstra
        d, _ = self.dijkstra(v)
        maior = max(d.items(), key=operator.itemgetter(1))
        
        return maior

    def DataReader(self, pathFile):   
        # Lê os dados do arquivo e adiciona as arestas ao grafo
        with open(pathFile, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[0] == 'a':
                    self.add_edge(data[1], data[2], int(data[3]))       
        # Escreve a lista de adjacência do grafo em um arquivo
        with open("db/USA-road-d.NY.gr_ListaAdjacencia.txt", 'w') as file:
            for chave, valor in self.listaAdjacencia.items():
                linha =  f"{chave}: {valor}\n"
                file.write(linha)
