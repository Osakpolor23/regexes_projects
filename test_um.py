import pytest
from um import count


def test_count():
    assert count("um") == 1
    assert count("electroluminescence") == 0
    assert count("mum") == 0
    assert count("gum") == 0
    assert count("rum") == 0
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("yum") == 0
    assert count("yummy") == 0
    assert count("Um, UM, um, I have forgotten, sorry") == 3