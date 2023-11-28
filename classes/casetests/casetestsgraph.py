from classes.entities.graph import Graph

class CaseTestsGraphs:
    
    def __init__(self, pathFile,isAdjacency=False):
        self.tests(isAdjacency, pathFile)
        
        
    def tests(self, isAdjacency, pathFile):
        graph = Graph(pathFile)
        print("Numero de arestas do grafo não direcionado: " , graph.n())
        print("----------------------------------------------------------------")
        print("Numero de vertices do grafo não direcionado: " , graph.m())
        print("----------------------------------------------------------------")
        print("O menor grau presente no grafo é : ", graph.mind())
        print("----------------------------------------------------------------")
        print("O maior grau presente no grafo é :", graph.maxd())
        print("----------------------------------------------------------------")
        print("Escolha qual vertice você deseja : ")
        vertice = str(input())
        print("----------------------------------------------------------------")
        print("Caminho de tamanho 10 ou superior para o vértice desejado é : ", graph.find_path_with_dijkstra(vertice))
            