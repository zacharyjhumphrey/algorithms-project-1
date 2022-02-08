# content of test_sample.py
from src.example import *


def func(x):
    return x + 1


def test_passing():
    assert Example().value == 7


def test_failing():
    assert Example().value < 4
