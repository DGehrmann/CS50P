import pytest
from um import count


def test_um_alone():
    assert count("um") == 1

def test_um_twice():
    assert count("um um") == 2

def test_um_case():
    assert count("Um") == 1

def test_um_words():
    assert count("This, um, is my album.") == 1