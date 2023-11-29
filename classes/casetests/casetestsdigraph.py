from classes.entities.digraph import Digraph

class CaseTestsDigraphs:
    
    def __init__(self, pathFile):
        self.tests(pathFile)
        
        
    def tests(self,pathFile):
        digraph = Digraph(pathFile)
        print("Numero de arestas do grafo não direcionado: " , digraph.n())
        print("----------------------------------------------------------------")
        print("Numero de vertices do grafo não direcionado: " , digraph.m())
        print("----------------------------------------------------------------")
        print("O menor grau presente no grafo é : ", digraph.mind())
        print("----------------------------------------------------------------")
        print("O maior grau presente no grafo é :", digraph.maxd())
        print("----------------------------------------------------------------")
        print("Escolha qual vertice você deseja : ")
        vertice = str(input())
        _, vertices = digraph.dijkstra(vertice)
        print("----------------------------------------------------------------")
        print("Caminho de tamanho 10 ou superior para o vértice desejado é : \n", sorted(digraph.encontre_caminho(vertices,10)))
        print("----------------------------------------------------------------")
        print("Ciclo com uma quantidade de arestas maior ou igual a 5 para o vertice é : \n", digraph.encontre_ciclos(vertices))
        print("----------------------------------------------------------------")
        print("O vértice mais distante do vértice 129 e sua distância entre eles é : \n", digraph.distance(vertice))
        print("----------------------------------------------------------------")
