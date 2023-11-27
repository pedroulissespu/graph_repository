from graph import Graph

#g = Graph("TesteAdjacencia.txt", adjacencyList=True)  # Choose the correct mode
#print(g.n())  # Number of vertices
#print(g.m())  # Number of edges

g = Graph("TesteAdjacencia.txt", True)
print("Numero de vertices : ",g.n(), "\n")
print("Numero de arestas : ",g.m(), "\n")
#print(g.mind())
#print(g.maxd())