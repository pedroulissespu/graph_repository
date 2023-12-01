from classes.casetests.casetestsgraph import CaseTestsGraphs
from classes.casetests.casetestsdigraph import CaseTestsDigraphs
import time
import os
 
# Função criada apenas para limpar a tela do terminal
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Caminho para o arquivo de dados do grafo
pathFile = "db/USA-road-d.NY.gr"

# Loop principal do programa
while True:
    # Menu de opções
    print("Selecione uma opção :")
    print("1 - Grafo não Direcionado\n2 - Digrafo\n3 - Sair")
    escolha = str(input())
    
    # Se a opção escolhida for 1, cria um objeto CaseTestsGraphs para um grafo não direcionado
    if int(escolha) == 1:
        casetestsgraphs = CaseTestsGraphs(pathFile)
        print("Pressione ENTER para continuar")
        pressioneEnter = str(input())
        limpar_tela()
        
    # Se a opção escolhida for 2, cria um objeto CaseTestsDigraphs para um digrafo
    elif int(escolha) == 2:
        casetestsdigraphs = CaseTestsDigraphs(pathFile)
        print("Pressione ENTER para continuar")
        pressioneEnter = str(input())
        limpar_tela()
        
    # Se a opção escolhida for 3, sai do programa
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
    
    # Se a opção escolhida não for válida, imprime uma mensagem de erro
    else:
        print("Selecione uma opção válida")
        print("Pressione ENTER para continuar")
        pressioneEnter = str(input())
        limpar_tela()
        
# Aguarda 2 segundos e fecha o terminal
time.sleep(2)
os.system('exit')