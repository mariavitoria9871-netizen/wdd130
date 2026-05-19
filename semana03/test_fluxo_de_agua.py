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