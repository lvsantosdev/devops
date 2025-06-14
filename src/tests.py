import pytest
import calculadora

def test_soma():
    assert calculadora.soma(2, 3) == 5
    assert calculadora.soma(-1, 1) == 0

def test_subtracao():
    assert calculadora.sub(5, 3) == 2
    assert calculadora.sub(3, 5) == -2

def test_multiplicacao():
    assert calculadora.mult(2, 3) == 6
    assert calculadora.mult(-1, 1) == -1

def test_divisao():
    assert calculadora.div(6, 3) == 2
    assert calculadora.div(5, 2) == 2.5
    with pytest.raises(ValueError):
        calculadora.div(5, 0)