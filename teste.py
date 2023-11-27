import ast

conteudo = """{
1: {('1363', 2428), ('12', 842), ('2', 803)},
2: {('48', 617), ('1', 803), ('13', 591)},
3: {('4', 158), ('3874', 1667)},
4: {('3937', 616), ('3926', 251), ('3', 158)},
5: {('1219', 3382), ('1204', 1921), ('6', 774), ('1214', 1345)},
}"""

# Convertendo a string em um dicionário
dicionario = ast.literal_eval(conteudo)

# Agora você pode acessar as chaves e valores do dicionário
for chave, valores in dicionario.items():
    print(f"Chave: {chave}")
    for valor in valores:
        print(f"Valores: {valor}")