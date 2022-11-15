from codigo.bytebank import Funcionario
import pytest
from pytest import mark

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

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given
        entrada_nome = 'Paulo Bragança'
        entrada_salario = 100000
        esperado = 90000
        funcionario_test = Funcionario(entrada_nome, '03/08/1994', entrada_salario)

        # When
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_receber_1000_deve_retornar_100(self):
        # Given
        entrada_salario = 1000
        esperado = 100
        funcionario_test = Funcionario('teste', '03/08/1994', entrada_salario)

        # When
        resultado = funcionario_test.calcular_bonus()

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_receber_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Given
            entrada_salario = 100000
            funcionario_test = Funcionario('teste', '03/08/1994', entrada_salario)

            # When
            resultado = funcionario_test.calcular_bonus()

            # Then
            assert resultado
