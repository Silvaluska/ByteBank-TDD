from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_03_08_1994_deve_retornar_28(self):
        # Given-Contexto
        entrada = '03/08/1994'
        esperado = 28
        funcionario_test =  Funcionario('teste', entrada, 10000)

        # When-Ação
        resultado = funcionario_test.idade()

        # Then-desfecho
        assert resultado == esperado

    def test_quando_nome_recebe_Lucas_silva_deve_retornar_silva(self):
        entrada = ' Lucas Silva '
        esperado = 'Silva'
        funcionario_test = Funcionario(entrada, '03/08/1994', 10000)

        resultado = funcionario_test.sobrenome()

        assert resultado == esperado


