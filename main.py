from classes.casetests.casetestsgraph import CaseTestsGraphs

print("Selecione uma opção :")
print("1 - Grafo não Direcionado        2 - Digrafo")
escolhaGrafo = int(input())

if escolhaGrafo == 1:
    pathFile = "db/USA-road-d.NY.gr.txt"
    casetestsgraphs = CaseTestsGraphs(pathFile)
else:
    pathFile = "db/USA-road-d.NY.gr.txt"
    casetestsgraphs = CaseTestsGraphs(pathFile)
