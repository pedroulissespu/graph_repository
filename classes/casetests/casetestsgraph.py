from classes.entities.graph import Graph

class CaseTestsGraphs:
    
    def __init__(self, pathFile):
        # Inicializa a classe e executa os testes
        self.tests(pathFile)
        
    def tests(self,pathFile):
        # Cria um objeto Graph e executa uma série de testes nele
        graph = Graph(pathFile)
        strTxT = ""
        print("Numero de arestas do grafo não direcionado: " , graph.n())
        strTxT += "Numero de arestas do grafo não direcionado: " + str(graph.n()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Numero de vertices do grafo não direcionado: " , graph.m())
        strTxT += "Numero de vertices do grafo não direcionado: " + str(graph.m()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("O menor grau presente no grafo é : ", graph.mind())
        strTxT += "O menor grau presente no grafo é : " + str(graph.mind()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("O maior grau presente no grafo é :", graph.maxd())
        strTxT += "O maior grau presente no grafo é :" + str(graph.maxd()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Escolha qual vertice você deseja : ")
        vertice = str(input())
        strTxT += "Vertice escolhido : " + vertice + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Caminho de tamanho 10 ou superior para o vértice desejado é : \n", graph.encontre_caminho(vertice,10))
        strTxT += "Caminho de tamanho 10 ou superior para o vértice desejado é : \n" + str(graph.encontre_caminho(vertice,10)) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Ciclo com uma quantidade de arestas maior ou igual a 5 para o vertice é : \n", graph.encontre_ciclos(vertice))
        strTxT += "Ciclo com uma quantidade de arestas maior ou igual a 5 para o vertice é : \n" + str(graph.encontre_ciclos(vertice)) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("O vértice mais distante do vértice 129 e sua distância entre eles é : \n", graph.distance(vertice))
        strTxT += "O vértice mais distante do vértice 129 e sua distância entre eles é : \n" + str(graph.distance(vertice)) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        
        with open('outputs/outputgraph.txt', 'w') as arquivo:
            arquivo.write(strTxT)
            