from classes.casetests.casetestsgraph import CaseTestsGraphs

print("Selecione uma opção :")
print("1 - Grafo não Direcionado        2 - Digrafo")
escolhaGrafo = int(input())
print("Escolha o formato de dados :")
print("1 - 1: {('1363', 2428), ('12', 842), ('2', 803)}         2 - a 1 2 803")
escolhaDados = int(input())

if escolhaGrafo == 1:
    if(escolhaDados == 1):
        pathFile = "db/USA-road-d.NY.gr_AdjacencyList.txt"
        casetestsgraphs = CaseTestsGraphs(pathFile, True)
    else:
        pathFile = "db/USA-road-d.NY.gr.txt"
        casetestsgraphs = CaseTestsGraphs(pathFile)
