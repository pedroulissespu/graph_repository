from classes.casetests.casetestsgraph import CaseTestsGraphs
from classes.casetests.casetestsdigraph import CaseTestsDigraphs
import time
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

pathFile = "db/USA-road-d.NY.gr.txt"
#pathFile = "db/teste.gr"

while True:
    print("Selecione uma opção :")
    print("1 - Grafo não Direcionado\n2 - Digrafo\n3 - Sair")
    escolha = str(input())
    
    if int(escolha) == 1:
        casetestsgraphs = CaseTestsGraphs(pathFile)
        print("Pressione ENTER para continuar")
        pressioneEnter = str(input())
        limpar_tela()
        
    elif int(escolha) == 2:
        casetestsdigraphs = CaseTestsDigraphs(pathFile)
        print("Pressione ENTER para continuar")
        pressioneEnter = str(input())
        limpar_tela()
        
    elif int(escolha) == 3:
        print("Saindo ")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Até a proxima")
        time.sleep(2)
        limpar_tela()
        break
    
    else:
        print("Selecione uma opção válida")
        print("Pressione ENTER para continuar")
        pressioneEnter = str(input())
        limpar_tela()
        
time.sleep(2)
os.system('exit')
