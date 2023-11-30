from classes.entities.digraph import Digraph

class CaseTestsDigraphs:
    
    def __init__(self, pathFile):
        # Inicializa a classe e executa os testes
        self.tests(pathFile)
        
    def tests(self,pathFile):
        # Cria um objeto Digraph e executa uma série de testes nele
        digraph = Digraph(pathFile)
        strTxT = ""
        print("Numero de arestas do Dígrafo ( Grafo Direcionado ): " , digraph.n())
        strTxT += "Numero de arestas do Dígrafo ( Grafo Direcionado ): " + str(digraph.n()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Numero de vertices do Dígrafo ( Grafo Direcionado ): " , digraph.m())
        strTxT += "Numero de vertices do Dígrafo ( Grafo Direcionado ): " + str(digraph.m()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("O menor grau presente no Dígrafo ( Grafo Direcionado ) é : ", digraph.mind())
        strTxT += "O menor grau presente no Dígrafo ( Grafo Direcionado ) é : " + str(digraph.mind()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("O maior grau presente no Dígrafo ( Grafo Direcionado ) é :", digraph.maxd())
        strTxT += "O maior grau presente no Dígrafo ( Grafo Direcionado ) é :" + str(digraph.maxd()) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Escolha qual vertice você deseja : ")
        vertice = str(input())
        _, vertices = digraph.dijkstra(vertice)
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Caminho de tamanho 10 ou superior para o vértice desejado é : \n", digraph.encontre_caminho(vertices,10))
        strTxT += "Caminho de tamanho 10 ou superior para o vértice desejado é : \n" + str(digraph.encontre_caminho(vertices,10)) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("Ciclo com uma quantidade de arestas maior ou igual a 5 para o vertice é : \n", digraph.encontre_ciclos(vertices))
        strTxT += "Ciclo com uma quantidade de arestas maior ou igual a 5 para o vertice é : \n" + str(digraph.encontre_ciclos(vertices)) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        print("O vértice mais distante do vértice 129 e sua distância entre eles é : \n", digraph.distance(vertice))
        strTxT += "O vértice mais distante do vértice 129 e sua distância entre eles é : \n" + str(digraph.distance(vertice)) + "\n"
        print("----------------------------------------------------------------")
        strTxT += "----------------------------------------------------------------\n"
        
        with open('outputs/outputdigraph.txt', 'w') as arquivo:
            arquivo.write(strTxT)
