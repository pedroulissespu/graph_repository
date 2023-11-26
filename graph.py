import collections
import math

class Graph:
    def __init__(self, pathFile, adjacencyList=False):
        self.vertices = {}
        self.edges = []
        self.DataReader(pathFile,adjacencyList)

    def add_vertex(self, v):
        self.vertices[v] = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
        self.vertices[u].append((v, w))
        self.vertices[v].append((u, w))

    def n(self):
        return len(self.vertices)

    def m(self):
        return len(self.edges)

    def viz(self, v):
        return [u for u, w in self.vertices[v]]

    def d(self, v):
        return len(self.vertices[v])

    def w(self, uv):
        u, v = uv
        for vertex, weight in self.vertices[u]:
            if vertex == v:
                return weight
        return None

    def mind(self):
        return min(len(v) for v in self.vertices.values())

    def maxd(self):
        return max(len(v) for v in self.vertices.values())

    def bfs(self, v):
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
        pi = {v: None}
        v_ini = {}
        v_fim = {}
        tempo = [0]

        def dfs_visit(u):
            tempo[0] += 1
            v_ini[u] = tempo[0]
            for vertex, weight in self.vertices[u]:
                if vertex not in v_ini:
                    pi[vertex] = u
                    dfs_visit(vertex)
            tempo[0] += 1
            v_fim[u] = tempo[0]

        dfs_visit(v)
        return pi, v_ini, v_fim

    def bf(self, v):
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
        d = {u: math.inf for u in self.vertices}
        d[v] = 0
        pi = {u: None for u in self.vertices}
        Q = set(self.vertices)

        while Q:
            u = min(Q, key=d.get)
            Q.remove(u)
            for vertex, weight in self.vertices[u]:
                alt = d[u] + weight
                if alt < d[vertex]:
                    d[vertex] = alt
                    pi[vertex] = u

        return d, pi
    
    def DataReader(self, pathFile, adjacencyList):
        if adjacencyList:
            lista_adjacencia = {}
            with open('arquivo.txt', 'r') as f:
                for linha in f:
                    chave, valor = linha.strip().split(':', 1)
                    lista_adjacencia[chave] = ast.literal_eval(valor.strip())
            
            TransformData(lista_adjacencia)
                        
        else:
            with open(pathFile, 'r') as file:
                for line in file:
                    data = line.strip().split()
                    if data[0] == 'a':
                        self.add_vertex(data[1])
                        self.add_vertex(data[2])
                        self.add_edge(data[1], data[2], int(data[3]))
        
        print(self.edges)
        
    def TransformData(listAdjacency):
        result = ""
        for 
        
        