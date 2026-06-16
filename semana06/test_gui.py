from gui import lancamento

def test_lancamento_um_dado():
    resultado = lancamento(6, 1)
    assert "Total:" in resultado
    assert len(resultado) > 0

def test_lancamento_varios_dados():
    resultado = lancamento(6, 3)
    assert "Total:" in resultado
    assert len(resultado.split()) >= 4

def test_lancamento_dois_dados():
    resultado = lancamento(20, 2)
    assert "Total:" in resultado
    assert "|" in resultado