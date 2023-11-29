from classes.entities.graph import Graph
import heapq
import sys
import math
from collections import deque

# Aumenta o limite de recursão do Python para evitar erros em grafos grandes
sys.setrecursionlimit(1000000000)

class Digraph(Graph):
    def __init__(self, pathFile=str):
        super().__init__(pathFile)
        
    def add_edge(self, u, v ,w):
        if u in self.listaAdjacencia.keys():
            if "positivo" in self.listaAdjacencia[u].keys():
                self.listaAdjacencia[u]["positivo"].append((v, w))
            else:
                self.listaAdjacencia[u].update({"positivo": [(v, w)]})
        else:
            self.listaAdjacencia.update({u: {"positivo": [(v, w)]}})
        if v in self.listaAdjacencia.keys():
            if "negativo" in self.listaAdjacencia[v].keys():
                self.listaAdjacencia[v]["negativo"].append((u, w))
            else:
                self.listaAdjacencia[v].update({"negativo": [(u, w)]})
        else:
            self.listaAdjacencia.update({v: {"negativo": [(u, w)]}})
            
    def viz(self, v):
        positivos, negativos = set(), set()
        
        for p in self.listaAdjacencia[v]["positivo"]:
            positivos.add(p)
        for n in self.listaAdjacencia[v]["negativo"]:
            negativos.add(n)
        
        return positivos, negativos
    
    def n(self):
        return len(self.listaAdjacencia.keys())
    
    def m(self):
        Arcs = 0
        for v in self.listaAdjacencia.keys():
            vizinhos = self.viz(v)
            Arcs += len(vizinhos[0])
            Arcs += len(vizinhos[1])
            
        return Arcs
    
    def d(self, v):
        vizP, vizN = self.viz(v)
        return len(vizP), len(vizN)
    
    def mind(self):
        return min([(self.d(v))[0] for v in self.listaAdjacencia.keys()]), min([(self.d(v))[1] for v in self.listaAdjacencia.keys()])
    
    def maxd(self):
        return max([(self.d(v))[0] for v in self.listaAdjacencia.keys()]), max([(self.d(v))[1] for v in self.listaAdjacencia.keys()])
    
    def encontre_caminho(self, v, T):
        # Conjunto de vértices testados e lista para armazenar o caminho
        testados, caminho = set(), []

        for vertice in self.listaAdjacencia.keys():

            # Se o vértice ainda não foi testado, o adicionamos ao caminho
            if vertice not in testados:

                # Marca o vértice como testado
                testados.add(vertice)

                # Obtém o pai do vértice usando a árvore T, gerada usando um dos algoritmos
                pai = v[vertice]

                # Enquanto houver um pai, o adicionamos a lista e atualizamos o pai
                while pai != None:
                    caminho.append(pai)
                    pai = v[pai]

                # Ao chegarmos na raiz, se o tamanho do caminho satisfizer a condição, retornamos o caminho.
                if len(caminho) >= T:
                    return caminho

                # Do contrário, o caminho é limpo e reiniciado
                else:
                    caminho.clear()
                    continue

        # Caso não haja um caminho com o valor requisitado
        return None
    
    def dijkstra(self, v):
        # Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto a partir de um vértice v
        d, antecessor, Q, visitado = {}, {}, [], set()

        [d.update({vert: 1000000000})for vert in self.listaAdjacencia.keys()]
        [antecessor.update({vert: None}) for vert in self.listaAdjacencia.keys()]

        d[v] = 0
        
        def relaxaDijkstra(d, antecessor, vertice):
            # Função auxiliar para o algoritmo de Dijkstra que relaxa as arestas
            vizinhos = self.viz(vertice)
            for vizinho, peso in vizinhos[0]:
                if d[vizinho] > d[vertice] + peso:
                    d[vizinho] = d[vertice] + peso
                    antecessor[vizinho] = vertice

        heapq.heappush(Q, v)

        while Q:
            vert = heapq.heappop(Q)  # B

            if vert in visitado:
                continue
            visitado.add(vert)

            relaxaDijkstra(d, antecessor, vert)
            vizinhos = self.viz(vert)
            for vizinho, _ in vizinhos[0]:
                if vizinho in visitado or vizinho in Q:
                    continue
                heapq.heappush(Q, vizinho)

        return d, antecessor
    
    def encontre_ciclos(self, v):
        # Encontra um ciclo de comprimento 50 a partir de um vértice v
        ciclos = self.encontre_caminho(v ,50)
        
        ciclosReverse = ciclos.copy()
        ciclosReverse.reverse()
        
        for vertice in ciclos:
            vizinhos = self.viz(vertice)
            for vizinho,_ in vizinhos[0]:
                if ciclosReverse[0] == vizinho:
                    index = ciclos.index(vertice)
                    if index >= 5:
                        ciclo = ciclosReverse[0:index]
                        ciclo.append(ciclosReverse[0])
                        return ciclo
    
    def bfs(self, s):
        color = {u: "white" for u in self.listaAdjacencia.keys()}
        d = {u: math.inf for u in self.listaAdjacencia.keys()}
        pi = {u: None for u in self.listaAdjacencia.keys()}
        color[s] = "gray"
        d[s] = 0
        Q = deque()
        Q.append(s)
        while Q:
            u = Q.popleft()
            for v, _ in self.listaAdjacencia[u]["positivo"]:
                if color[v] == "white":
                    color[v] = "gray"
                    d[v] = d[u] + 1
                    pi[v] = u
                    Q.append(v)
            color[u] = "black"
        return d, pi

    def dfs_visit(self, u, color, d, f, pi, time):
        time += 1
        d[u] = time
        color[u] = "gray"
        for v, _ in self.listaAdjacencia[u]["positivo"]:
            if color[v] == "white":
                pi[v] = u
                time = self.dfs_visit(v, color, d, f, pi, time)
        color[u] = "black"
        time += 1
        f[u] = time
        return time

    def dfs(self, s):
        color = {u: "white" for u in self.listaAdjacencia.keys()}
        pi = {u: None for u in self.listaAdjacencia.keys()}
        d = {u: float('inf') for u in self.listaAdjacencia.keys()}
        f = {u: float('inf') for u in self.listaAdjacencia.keys()}
        time = 0
        if color[s] == "white":
            time = self.dfs_visit(s, color, d, f, pi, time)
        return pi, d, f

    def bf(self, s):
        d = {u: math.inf for u in self.listaAdjacencia.keys()}
        pi = {u: None for u in self.listaAdjacencia.keys()}
        d[s] = 0
        for _ in range(len(self.listaAdjacencia) - 1):
            for u in self.listaAdjacencia.keys():
                for v, w in self.listaAdjacencia[u]["positivo"]:
                    if d[u] + w < d[v]:
                        d[v] = d[u] + w
                        pi[v] = u
        for u in self.listaAdjacencia.keys():
            for v, w in self.listaAdjacencia[u]["positivo"]:
                if d[u] + w < d[v]:
                    return False  # Existe um ciclo de peso negativo
        return d, pi
    