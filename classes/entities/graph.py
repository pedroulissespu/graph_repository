import collections
import math
import heapq

class Graph:
    def __init__(self, pathFile=str):
        self.listaAdjacencia = {}
        self.DataReader(pathFile)

    def add_edge(self, u, v, w):      
        if u in self.listaAdjacencia.keys():
            self.listaAdjacencia[u].append((v, w))
        else:
            self.listaAdjacencia.update({u: [(v, w)]})

        if v in self.listaAdjacencia.keys():
                self.listaAdjacencia[v].append((u, w))
        else:
            self.listaAdjacencia.update({v: [(u, w)]})

    def n(self):
        return len(self.listaAdjacencia.keys())

    def m(self):
        edges = 0
        
        for vertice, neighbors in self.listaAdjacencia.items():
            edges += len(neighbors)
        
        return edges // 2

    def viz(self, v):
        if v in self.listaAdjacencia:
            return self.listaAdjacencia[v]
        else:
            return []

    def d(self, v):
        return len(self.viz(v))

    def w(self, uv):
        u, v = uv
        for vertex, weight in self.vertices[u]:
            if vertex == v:
                return weight
        return None

    def mind(self):
        return min([self.d(vertex) for vertex in self.listaAdjacencia.keys()])

    def maxd(self):
        return max([self.d(vertex) for vertex in self.listaAdjacencia.keys()])

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
        d = {v: float('inf') for v in self.listaAdjacencia}
        pi = {v: None for v in self.listaAdjacencia}
        
        d[v] = 0
        
        priority_queue = [(0, v)]
        
        while priority_queue:
            d_v, vertex = heapq.heappop(priority_queue)
            
            for u, w in self.listaAdjacencia[vertex]:
                new_d = d_v + w
                if new_d < d[u]:
                    d[u] = new_d
                    pi[u] = vertex
                    heapq.heappush(priority_queue, (new_d, u))
                    
        return d, pi
    
    def find_path(self, v, T):
        path = []
        init = v
        
        while T[init] is not None:
            path.insert(0, init)
            init = T[init]
            
        path.insert(0, init)
        
        if len(path) < 10:
            print("O caminho não possui mais que 10 arestas")
            return None
        else:
            return path
    
    def find_path_with_dijkstra(self, v):
        d, pi = self.dijkstra(v)
        path = self.find_path(v, pi)
        return d, path
    
    def DataReader(self, pathFile):
        """with open(pathFile, 'r') as file:
            for line in file:
                result = "{"
                result += re.sub(r"(\w+):", r"'\1':", line)
                result += "}"
                listDict = {}
                listDict = ast.literal_eval(result)
                print(listDict)
                for chave, valores in listDict.items():
                    for valor in valores:
                        vertex,peso = valor
                        self.add_vertex(str(chave))
                        self.add_vertex(str(vertex))
                        self.add_edge(str(chave), str(vertex), int(peso))"""
               
        with open(pathFile, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[0] == 'a':
                    self.add_edge(data[1], data[2], int(data[3]))
        
        #print(self.listaAdjacencia)
