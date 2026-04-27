import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import divide, multiplica, soma, subtrai


def test_soma_dois_positivos():
    assert soma(2, 3) == 5


def test_soma_com_zero():
    assert soma(0, 7) == 7


def test_subtrai_resultado_positivo():
    assert subtrai(10, 4) == 6


def test_multiplica_numeros_inteiros():
    assert multiplica(3, 4) == 12


def test_divide_resultado_correto():
    assert divide(10, 2) == 5


def test_divide_por_zero_lanca_excecao():
    with pytest.raises(ValueError):
        divide(10, 0)
