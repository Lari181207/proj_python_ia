lista = [1,6,9]
tupla = [3,7,8]
dicionario = {
    "Professor": "Gustavo",
    "Disciplina": "Versionamento",
    "Aluno":"Felipe",
    "Ano":2024
    }
print(lista[2])
print(tupla[2])
print(dicionario.keys())
print(type(dicionario))
for x in dicionario.values():
    print("{:>10} {:>10}".format(x.keys(),x.values()))
    

