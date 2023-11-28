from classes.casetests.casetestsgraph import CaseTestsGraphs
pathFile = "db/USA-road-d.NY.gr.txt"

print("Selecione uma opção :")
print("1 - Grafo não Direcionado        2 - Digrafo        3 - Sair")
escolhaGrafo = str(input())

if int(escolhaGrafo) == 1:
    casetestsgraphs = CaseTestsGraphs(pathFile)
elif int(escolhaGrafo) == 2:
    casetestsgraphs = CaseTestsGraphs(pathFile)
