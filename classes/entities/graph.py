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
        edges = set()
        
        for edge in self.listaAdjacencia.values():
            for item in edge:
                edges.add(item)
        
        return len(edges)

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
        """
        Retorna o peso de uma aresta.

        Parâmetros:
        uv (tuple): Uma tupla contendo os vértices da aresta (u, v).

        Retorna:
        int or None: O peso da aresta se existir, caso contrário retorna None.
        """
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
        """
        Realiza uma busca em largura a partir de um vértice v, retornando a distância e o predecessor de cada vértice.

        Parâmetros:
        - v: O vértice inicial da busca.

        Retorno:
        - d: Um dicionário contendo a distância de cada vértice em relação ao vértice inicial.
        - pi: Um dicionário contendo o predecessor de cada vértice na busca.

        Lógica:
        - Inicializa as estruturas de dados d e pi com o vértice inicial v.
        - Cria uma fila vazia e adiciona o vértice inicial v.
        - Enquanto a fila não estiver vazia:
            - Remove o primeiro elemento da fila e o atribui a u.
            - Para cada vértice adjacente a u:
                - Se o vértice ainda não foi visitado:
                    - Atualiza a distância e o predecessor do vértice adjacente.
                    - Adiciona o vértice adjacente à fila.
        - Retorna os dicionários d e pi.
        """
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
        """
        Realiza uma busca em profundidade a partir de um vértice v, retornando o predecessor e os tempos de início e fim de cada vértice.

        Parâmetros:
            - v: O vértice inicial da busca em profundidade.

        Retorno:
            - predecessor: Um dicionário que mapeia cada vértice ao seu predecessor na busca em profundidade.
            - tempo_inicio: Um dicionário que mapeia cada vértice ao seu tempo de início na busca em profundidade.
            - tempo_fim: Um dicionário que mapeia cada vértice ao seu tempo de fim na busca em profundidade.
        """
        visitado = {x: False for x in self.listaAdjacencia}
        tempo_inicio = {x: None for x in self.listaAdjacencia}
        tempo_fim = {x: None for x in self.listaAdjacencia}
        predecessor = {x: None for x in self.listaAdjacencia}
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
        """
        Encontra um caminho de comprimento T a partir de um vértice v usando busca em profundidade.

        Args:
            v (int): O vértice inicial.
            T (int): O comprimento do caminho desejado.

        Returns:
            list or None: Uma lista contendo o caminho encontrado ou None caso nenhum caminho seja encontrado.
        """

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
        """
        Encontra um ciclo de comprimento 50 a partir de um vértice v.

        Args:
            v (int): O vértice inicial para encontrar o ciclo.

        Returns:
            list: O ciclo encontrado.

        """
        # Encontra um caminho de comprimento 50 a partir do vértice v
        ciclos = self.encontre_caminho(v, 50)
            
        # Cria uma cópia reversa do caminho encontrado
        ciclosReverse = ciclos.copy()
        ciclosReverse.reverse()
            
        # Verifica se o primeiro vértice do caminho reverso é vizinho do último vértice do caminho original
        for vertice in ciclos:
            vizinhos = self.viz(vertice)
            for vizinho, _ in vizinhos:
                if ciclosReverse[0] == vizinho:
                    # Encontra o índice do vértice atual no caminho original
                    index = ciclos.index(vertice)
                    if index >= 5:
                        # Cria um ciclo com os vértices do caminho reverso até o vértice atual
                        ciclo = ciclosReverse[0:index]
                        ciclo.append(ciclosReverse[0])
                        return ciclo

    def bf(self, v):
        """
        Implementa o algoritmo de Bellman-Ford para encontrar o caminho mais curto a partir de um vértice v.

        Parâmetros:
            v (int): O vértice de origem para calcular os caminhos mais curtos.

        Retorna:
            d (dict): Um dicionário contendo os caminhos mais curtos a partir do vértice de origem v.
            pi (dict): Um dicionário contendo os predecessores de cada vértice no caminho mais curto a partir de v.

        Lança:
            ValueError: Se o grafo contiver um ciclo de peso negativo.
        """
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
                raise ValueError("O grafo contém um ciclo de peso negativo")

        return d, pi

    def dijkstra(self, v):
        """
        Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto a partir de um vértice v.

        Args:
            v (int): O vértice de partida.

        Returns:
            tuple: Uma tupla contendo dois dicionários. O primeiro dicionário contém as distâncias mínimas
                   de cada vértice até o vértice de partida. O segundo dicionário contém os antecessores de
                    cada vértice no caminho mais curto até o vértice de partida.
        """
        d, antecessor, Q, visitado = {}, {}, [], set()

        [d.update({vert: 1000000000})for vert in self.listaAdjacencia.keys()]
        [antecessor.update({vert: None}) for vert in self.listaAdjacencia.keys()]

        d[v] = 0
            
        def relaxaDijkstra(d, antecessor, vertice):
            """
            Função auxiliar para o algoritmo de Dijkstra que relaxa as arestas.

            Args:
                d (dict): Dicionário contendo as distâncias mínimas de cada vértice até o vértice de partida.
                antecessor (dict): Dicionário contendo os antecessores de cada vértice no caminho mais curto até o vértice de partida.
                vertice (int): O vértice atual.

            Returns:
                None
            """
            vizinhos = self.viz(vertice)
            for vizinho, peso in vizinhos:
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
            for vizinho, _ in vizinhos:
                if vizinho in visitado or vizinho in Q:
                    continue
                heapq.heappush(Q, vizinho)

        return d, antecessor

    def distance(self, v):
        """
        Retorna o vértice mais distante a partir de um vértice v usando o algoritmo de Dijkstra.

        Parâmetros:
        - v: O vértice de partida.

        Retorna:
        - O vértice mais distante a partir do vértice de partida.
        """
        d, _ = self.dijkstra(v)
        maior = max(d.items(), key=operator.itemgetter(1))
        
        return maior

    def DataReader(self, pathFile):
        """
        Lê os dados de um arquivo e adiciona as arestas ao grafo.

        Args:
            pathFile (str): O caminho do arquivo a ser lido.

        Returns:
            None
        """
        with open(pathFile, 'r') as file:
            for line in file:
                if line.strip().split():
                    data = line.strip().split()
                    if data[0] == 'a':
                        self.add_edge(data[1], data[2], int(data[3]))

        # Escreve a lista de adjacência do grafo em um arquivo
        for item in self.listaAdjacencia.items():
            print(item)
        with open("db/USA-road-d.NY_ListaAdjacencia.gr", 'w') as file:
            for chave, valor in self.listaAdjacencia.items():
                linha = f"{chave}: {valor}\n"
                file.write(linha)
