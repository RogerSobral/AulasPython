usuarios=[
# Coluna    0        1   2
          ["Carlos",23,"11 3434-3434"],#linha 0
          ["pedro",23,"11 3434-3434"],#linha 1
          ["Rony",44,"11 3434-3434"],#linha 2
          ["Tereza",18,"11 3434-3434"],#linha 3
]



for index,linha in enumerate(usuarios):
    # rodada 1:  linha = ["Carlos",23,"11 3434-3434"] 0
    # rodada 2:  linha = ["pedro",23,"11 3434-3434"]
    # rodada 3:  linha = ["Rony",44,"11 3434-3434"]
    # rodada 4:  linha = ["Tereza",18,"11 3434-3434"]
    print(f"Linha: {linha} Index:{index}")
print("#"*40)

usuarios.pop(1)

for index,linha in enumerate(usuarios):
    # rodada 1:  linha = ["Carlos",23,"11 3434-3434"] 0
    # rodada 2:  linha = ["Rony",44,"11 3434-3434"]
    # rodada 3:  linha = ["Tereza",18,"11 3434-3434"]
    print(f"Linha: {linha} Index:{index}")
