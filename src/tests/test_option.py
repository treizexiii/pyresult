import pytest
from pyresult import Some, None_, Option

# Test de la création et des états

def test_is_some_is_none():
    assert Some(10).is_some() is True
    assert Some(10).is_none() is False
    assert None_().is_some() is False
    assert None_().is_none() is True

# Test des fonctions unwrap

def test_unwrap():
    assert Some(42).unwrap() == 42
    assert Some(42).unwrap_or(100) == 42
    assert None_().unwrap_or(100) == 100

    with pytest.raises(ValueError, match="Called unwrap() on a None"):
        None_().unwrap()

# Test des transformations

def test_map():
    assert Some(10).map(lambda x: x * 2) == Some(20)
    assert None_().map(lambda x: x * 2) == None_()

# Test des fonctions combinatoires

def test_and_then():
    assert Some(10).and_then(lambda x: Some(x * 2)) == Some(20)
    assert None_().and_then(lambda x: Some(x * 2)) == None_()

# Test de filter

def test_filter():
    assert Some(10).filter(lambda x: x > 5) == Some(10)
    assert Some(10).filter(lambda x: x < 5) == None_()
    assert None_().filter(lambda x: x > 5) == None_()

# Test de map_or

def test_map_or():
    assert Some(10).map_or(100, lambda x: x * 2) == 20
    assert None_().map_or(100, lambda x: x * 2) == 100

# Test de expect

def test_expect():
    assert Some(42).expect("Value expected") == 42

    with pytest.raises(ValueError, match="Value expected"):
        None_().expect("Value expected")

# Test du pattern matching

def test_match_option():
    option = Some(42)
    match option:
        case Some(value):
            assert value == 42
        case None_():
            assert False

    option = None_()
    match option:
        case Some(value):
            assert False
        case None_():
            assert True
