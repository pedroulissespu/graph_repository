from classes.entities.graph import Graph

class CaseTestsGraphs:
    
    def __init__(self, pathFile,isAdjacency=False):
        self.tests(isAdjacency, pathFile)
        
        
    def tests(self, isAdjacency, pathFile):
        if isAdjacency:
            graph = Graph(pathFile, isAdjacency)
            print("Numero de arestas do grafo : " , graph.n())
            print("Numero de vertices do grafo : " , graph.m())
            print("O menor grau presente no grafo é : ", graph.mind())
            print("O maior grau presente no grafo é :", graph.maxd())
        #else:
            