from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Lucas Silva', '03/08/1994', 10000)
    print(f'teste = {funcionario_teste.idade()}')

teste_idade()