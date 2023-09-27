import requests

def buscarCEP(cep):

    cep = cep.replace("-", "").replace(".", "").replace(" ", "")


    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)



    resposta = requisicao.json()

    if len(resposta) == 10:
        uf = resposta['uf']
        cidade = resposta['localidade']
        bairro = resposta['bairro']
        ibge = resposta['ibge']
        comp = resposta['complemento']
        rua = resposta['logradouro']

    else:
        uf = ""
        cidade = ""
        bairro = ""
        ibge = ""
        comp = ""
        rua = ""
    return uf, cidade, rua, bairro, ibge, comp