from pytest import approx
import pytest
from fluxo_de_agua import *

def test_calc_altura_coluna_agua():
    assert calc_altura_coluna_agua(0.0, 0.0) == 0.0
    assert calc_altura_coluna_agua(0.0, 10.0) == 7.5
    assert calc_altura_coluna_agua(25.0, 0.0) == 25.0
    assert calc_altura_coluna_agua(48.3, 12.8) == 57.9

def test_calc_pressao_pela_altura():
    assert calc_pressao_pela_altura(0.0) == approx(0.000, abs=0.001)
    assert calc_pressao_pela_altura(30.2) == approx(295.628, abs=0.001)
    assert calc_pressao_pela_altura(50.0) == approx(489.450, abs=0.001)

def test_calc_perda_pressao_tubo():
    assert calc_perda_pressao_tubo(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.018, 1.75) == approx(-133.008, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.0, 0.018, 1.65) == approx(-100.462, abs=0.001)

def test_calc_perda_pressao_conexoes():
    assert calc_perda_pressao_conexoes(0.0, 4) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 0) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 4) == approx(-0.217, abs=0.001)


def test_calc_num_reynolds():
    assert calc_num_reynolds(0.048692, 0.0) == approx(0.000, abs=0.001)
    assert calc_num_reynolds(0.048692, 1.65) == approx(80069.074, abs=0.001)


def test_calc_perda_pressao_reducao_tubo():
    reynolds = calc_num_reynolds(0.28687, 1.65)
    assert calc_perda_pressao_reducao_tubo(0.28687, 1.65, reynolds, 0.048692) == approx(-164.016, abs=0.001)


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
