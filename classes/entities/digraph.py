from classes.entities.graph import Graph
import heapq
import sys
import math
from collections import deque

# Aumenta o limite de recursão do Python para evitar erros em grafos grandes
sys.setrecursionlimit(1000000000)

class Digraph(Graph):
    def __init__(self, pathFile=str):
        # Chama o construtor da classe pai (Graph)
        super().__init__(pathFile)
        
    def add_edge(self, u, v ,w):
        """
        Adiciona uma aresta direcionada ao grafo.

        Args:
            u (any): Vértice de origem da aresta.
            v (any): Vértice de destino da aresta.
            w (any): Peso da aresta.

        Explanation:
            Esta função adiciona uma aresta direcionada ao grafo. 
            Uma aresta direcionada vai de um vértice 'u' para um vértice 'v', 
            mas não necessariamente na direção oposta. 

            A lógica do código verifica se o vértice 'u' já está presente no dicionário de adjacência.
            Se estiver presente, verifica se já existe uma lista de arestas positivas ('positivo') associada a 'u'.
            Se existir, a nova aresta é adicionada a essa lista. Caso contrário, uma nova lista é criada e a nova aresta é adicionada a ela.

            Se o vértice 'v' já estiver presente no dicionário de adjacência, a lógica é a mesma, mas para as arestas negativas ('negativo').

            Se o vértice 'u' ou 'v' não estiverem presentes no dicionário de adjacência, eles são adicionados como chaves no dicionário,
            e uma nova lista de arestas é criada e associada a eles.

        """
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
        """
        Retorna os vizinhos de um vértice. Em um digrafo, um vértice tem vizinhos "positivos" 
        (para onde ele tem arestas) e "negativos" (de onde ele recebe arestas).
            
        Parâmetros:
            v (int): O vértice para o qual se deseja obter os vizinhos.
            
        Retorna:
            tuple: Uma tupla contendo dois conjuntos, o primeiro com os vizinhos positivos e o segundo com os vizinhos negativos.
        """
        positivos, negativos = set(), set()
            
        for p in self.listaAdjacencia[v]["positivo"]:
            positivos.add(p)
        for n in self.listaAdjacencia[v]["negativo"]:
            negativos.add(n)
            
        return positivos, negativos
    
    def n(self):
        # Retorna o número de vértices no grafo
        return len(self.listaAdjacencia.keys())
    
    def m(self):
        """
        Retorna o número de arestas no grafo.

        A função percorre todos os vértices do grafo e conta o número de arestas
        que estão conectadas a cada vértice. Em seguida, retorna a soma total
        de todas as arestas encontradas.

        Returns:
            int: O número de arestas no grafo.
        """
        Arcs = 0
        for v in self.listaAdjacencia.keys():
            vizinhos = self.viz(v)
            Arcs += len(vizinhos[0])
            Arcs += len(vizinhos[1])
                
        return Arcs
    
    def d(self, v):
        """
        Retorna o grau de um vértice (número de vizinhos). Em um digrafo, um vértice tem grau "positivo" 
        (número de arestas que saem dele) e "negativo" (número de arestas que chegam nele).
        
        Parâmetros:
        - v: O vértice para o qual se deseja obter o grau.
        
        Retorna:
        - Um par de valores, representando o grau positivo e o grau negativo do vértice.
        """
        vizP, vizN = self.viz(v)
        return len(vizP), len(vizN)
    
    def w(self, uv):
        """
        Retorna o peso da aresta entre dois vértices.

        Parâmetros:
        - vertice_origem: O vértice de origem da aresta.
        - vertice_destino: O vértice de destino da aresta.

        Retorna:
        - O peso da aresta se ela existir.
        - None se a aresta não existir.
        """
        # Verifica se a aresta existe
        u, v = uv
        if v in self.listaAdjacencia[u]:
            return self.listaAdjacencia[u][v]
        else:
            return None  # Retorna None se a aresta não existe
    
    def mind(self):
        # Retorna o menor grau entre todos os vértices do grafo
        return min([(self.d(v))[0] for v in self.listaAdjacencia.keys()]), min([(self.d(v))[1] for v in self.listaAdjacencia.keys()])
    
    def maxd(self):
        # Retorna o maior grau entre todos os vértices do grafo
        return max([(self.d(v))[0] for v in self.listaAdjacencia.keys()]), max([(self.d(v))[1] for v in self.listaAdjacencia.keys()])
    
    def encontre_caminho(self, v, T):
        """
        Encontra um caminho no grafo a partir de um vértice de origem, seguindo a árvore T gerada pelo algoritmo de Dijkstra.

        Args:
            v (dict): Dicionário que mapeia cada vértice do grafo ao seu pai na árvore T.
            T (int): Tamanho mínimo do caminho desejado.

        Returns:
            list: Lista contendo o caminho encontrado, se existir, ou None caso contrário.
        """

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
        """
        Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto a partir de um vértice v.

        Args:
            v (int): O vértice de partida.

        Returns:
            tuple: Uma tupla contendo dois dicionários. O primeiro dicionário contém as distâncias mínimas
                   de cada vértice em relação ao vértice de partida. O segundo dicionário contém os antecessores
                   de cada vértice no caminho mais curto.

        """
        d, antecessor, Q, visitado = {}, {}, [], set()

        [d.update({vert: 1000000000})for vert in self.listaAdjacencia.keys()]
        [antecessor.update({vert: None}) for vert in self.listaAdjacencia.keys()]

        d[v] = 0
            
        def relaxaDijkstra(d, antecessor, vertice):
            """
            Função auxiliar para o algoritmo de Dijkstra que relaxa as arestas.
                
            Args:
                d (dict): Dicionário contendo as distâncias mínimas de cada vértice.
                antecessor (dict): Dicionário contendo os antecessores de cada vértice.
                vertice (int): O vértice atual.

            """
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
        """
        Encontra um ciclo de comprimento 50 a partir de um vértice v.

        Args:
            v (int): O vértice inicial para iniciar a busca do ciclo.

        Returns:
            list: Uma lista contendo os vértices do ciclo encontrado.
        """
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
        """
        Realiza uma busca em largura a partir de um vértice s, retornando a distância e o predecessor de cada vértice.

        Parâmetros:
            - s: O vértice de partida da busca.

        Retorno:
            - d: Um dicionário contendo a distância de cada vértice em relação ao vértice de partida.
            - pi: Um dicionário contendo o predecessor de cada vértice na busca.

        Lógica:
            1. Inicialize as estruturas de dados necessárias: color, d, pi e Q.
            2. Defina a cor do vértice de partida como "gray", a distância como 0 e o predecessor como None.
            3. Adicione o vértice de partida à fila Q.
            4. Enquanto a fila Q não estiver vazia:
                - Remova o primeiro vértice da fila Q.
                - Para cada vértice adjacente v ao vértice removido:
                    - Se v ainda não foi visitado (cor "white"):
                        - Marque v como visitado (cor "gray").
                        - Atualize a distância de v como a distância de u + 1.
                        - Defina o predecessor de v como u.
                        - Adicione v à fila Q.
                - Marque o vértice removido como visitado (cor "black").
            5. Retorne os dicionários d e pi contendo a distância e o predecessor de cada vértice, respectivamente.
        """
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
        """
        Realiza uma visita em profundidade (DFS) a partir de um vértice u em um grafo direcionado.
            
        Parâmetros:
            - u: O vértice inicial da visita.
            - color: Um dicionário que armazena a cor de cada vértice do grafo.
            - d: Um dicionário que armazena o tempo de descoberta de cada vértice.
            - f: Um dicionário que armazena o tempo de finalização de cada vértice.
            - pi: Um dicionário que armazena o predecessor de cada vértice na árvore de busca em profundidade.
            - time: O tempo atual da visita em profundidade.
            
        Retorna:
            - O tempo atualizado da visita em profundidade.
        """
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
        """
        Realiza uma busca em profundidade a partir de um vértice s, retornando o predecessor e os tempos de início e fim de cada vértice.

        Parâmetros:
        - s: O vértice inicial da busca em profundidade.

        Retorno:
        - pi: Um dicionário contendo o predecessor de cada vértice visitado durante a busca em profundidade.
        - d: Um dicionário contendo o tempo de início de cada vértice visitado durante a busca em profundidade.
        - f: Um dicionário contendo o tempo de fim de cada vértice visitado durante a busca em profundidade.
        """

        color = {u: "white" for u in self.listaAdjacencia.keys()}
        pi = {u: None for u in self.listaAdjacencia.keys()}
        d = {u: float('inf') for u in self.listaAdjacencia.keys()}
        f = {u: float('inf') for u in self.listaAdjacencia.keys()}
        time = 0
        if color[s] == "white":
            time = self.dfs_visit(s, color, d, f, pi, time)
        return pi, d, f

    def bf(self, s):
        """
        Implementa o algoritmo de Bellman-Ford para encontrar o caminho mais curto a partir de um vértice s.

        Parâmetros:
        - s: O vértice de origem para calcular o caminho mais curto.

        Retorna:
        - Um dicionário contendo as distâncias mínimas de cada vértice em relação ao vértice de origem s.
        - Um dicionário contendo os predecessores de cada vértice no caminho mais curto em relação ao vértice de origem s.
        - False, se houver um ciclo de peso negativo no grafo.
        """
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
    