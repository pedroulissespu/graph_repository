from classes.entities.graph import Graph

class CaseTestsGraphs:
    
    def __init__(self, pathFile):
        # Inicializa a classe e executa os testes
        self.tests(pathFile)
        
    def tests(self,pathFile):
        # Cria um objeto Graph e executa uma série de testes nele
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
        print("Caminho de tamanho 10 ou superior para o vértice desejado é : \n", graph.encontre_caminho(vertice,10))
        print("----------------------------------------------------------------")
        print("Ciclo com uma quantidade de arestas maior ou igual a 5 para o vertice é : \n", graph.encontre_ciclos(vertice))
        print("----------------------------------------------------------------")
        print("O vértice mais distante do vértice 129 e sua distância entre eles é : \n", graph.distance(vertice))
        print("----------------------------------------------------------------")