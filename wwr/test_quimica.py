# Direitos Autorais 2020, Brigham Young University-Idaho. Todos os direitos reservados.

from wwr.quimica import criar_tabela_periodica, calcular_massa_molar
from wwr.formula import interpretar_formula, FormulaError
from pytest import approx
import pytest

def test_interpretar_formula():
    """Verifica se a função interpretar_formula funciona corretamente.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    # Chame a função criar_tabela_periodica
    # e verifique se ela retorna um dicionário.
    dic_tabela = criar_tabela_periodica()
    assert isinstance(dic_tabela, dict), \
        "A função criar_tabela_periodica deve retornar um dicionário: " \
        f"era esperado um dicionário, mas foi encontrado um {type(dic_tabela)}"

    # Chame a função interpretar_formula e
    # verifique se ela retorna uma lista.
    lista_quantidade_simbolos = interpretar_formula("H2O", dic_tabela)
    assert isinstance(lista_quantidade_simbolos, list), \
        "A função interpretar_formula deve retornar uma lista: " \
        f"era esperado uma lista, mas foi encontrado um {type(lista_quantidade_simbolos)}"

    # Chame a função interpretar_formula quatro vezes e
    # verifique se ela retorna os valores corretos.
    assert interpretar_formula("H2O", dic_tabela) == [("H", 2), ("O", 1)]
    assert interpretar_formula("C6H6", dic_tabela) == [("C", 6), ("H", 6)]
    assert interpretar_formula("(C2(NaCl)4H2)2C4Na", dic_tabela) == [("C", 8), ("Na", 9), ("Cl", 8), ("H", 4)]
    assert interpretar_formula("Co", dic_tabela) == [("Co", 1)]

    # Chame a função interpretar_formula seis vezes com fórmulas inválidas
    # e verifique se a função lança exceção em cada caso.
    with pytest.raises(FormulaError):
        interpretar_formula("L", dic_tabela)
    with pytest.raises(FormulaError):
        interpretar_formula("4H", dic_tabela)
    with pytest.raises(FormulaError):
        interpretar_formula("H2L4", dic_tabela)
    with pytest.raises(FormulaError):
        interpretar_formula("-H", dic_tabela)
    with pytest.raises(FormulaError):
        interpretar_formula("(H2O", dic_tabela)
    with pytest.raises(FormulaError):
        interpretar_formula("H2)O3", dic_tabela)


def test_calcular_massa_molar():
    """Verifica se a função calcular_massa_molar funciona corretamente.

    Parâmetros: nenhum
    Retorno: nenhum
    """
    # Chame a função criar_tabela_periodica
    # e verifique se ela retorna um dicionário.
    dic_tabela = criar_tabela_periodica()
    assert isinstance(dic_tabela, dict), \
        "A função criar_tabela_periodica deve retornar um dicionário: " \
        f"era esperado um dicionário, mas foi encontrado um {type(dic_tabela)}"

    # Chame a função calcular_massa_molar
    # e verifique se ela retorna um número.
    massa = calcular_massa_molar([["O", 2]], dic_tabela)
    assert isinstance(massa, (int, float)), \
        "A função calcular_massa_molar deve retornar um número: " \
        f"era esperado um número, mas foi encontrado um {type(massa)}"

    # Chame a função calcular_massa_molar quatro vezes e
    # verifique se ela retorna os valores corretos.
    assert calcular_massa_molar([], dic_tabela) == 0
    assert calcular_massa_molar([["O", 2]], dic_tabela) == approx(31.9988)
    assert calcular_massa_molar([["C", 6], ["H", 6]], dic_tabela) == approx(78.11184)
    assert calcular_massa_molar([["C", 13], ["H", 16], ["N", 2], ["O", 2]], dic_tabela) == approx(232.27834)
