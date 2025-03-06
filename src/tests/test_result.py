import pytest
import re
from pyresult import Result, Ok, Err

# Test de la création et des états

def test_is_ok_is_err():
    assert Ok(10).is_ok() is True
    assert Ok(10).is_err() is False
    assert Err("Error").is_ok() is False
    assert Err("Error").is_err() is True

# Test des fonctions unwrap

def test_unwrap():
    assert Ok(42).unwrap() == 42
    assert Ok(42).unwrap_or(100) == 42
    assert Err("Error").unwrap_or(100) == 100

    with pytest.raises(ValueError, match=re.escape("Called unwrap() on an Err: Error")):
        Err("Error").unwrap()

def test_unwrap_err():
    assert Err("Failure").unwrap_err() == "Failure"

    with pytest.raises(ValueError, match=re.escape("Called unwrap_err() on an Ok: 42")):
        Ok(42).unwrap_err()

# Test des transformations

def test_map():
    assert Ok(10).map(lambda x: x * 2) == Ok(20)
    assert Err("Error").map(lambda x: x * 2) == Err("Error")

def test_map_err_noop():
    assert Ok(10).map_error(lambda e: f"Error: {e}") == Ok(10)

def test_map_error():
    assert Err("Oops").map_error(lambda e: f"Error: {e}") == Err("Error: Oops")

# Test des fonctions combinatoires

def test_and_then():
    assert Ok(10).and_then(lambda x: Ok(x * 2)) == Ok(20)
    assert Err("Error").and_then(lambda x: Ok(x * 2)) == Err("Error")

def test_and_then_to_err():
    assert Ok(10).and_then(lambda x: Err("Failure")) == Err("Failure")

def test_or_else():
    assert Err("Oops").or_else(lambda e: Ok(100)) == Ok(100)
    assert Err("Oops").or_else(lambda e: Err(f"Error: {e}")) == Err("Error: Oops")

# Test du pattern matching

def test_match_result():
    result = Ok(42)
    match result:
        case Ok(value):
            assert value == 42
        case Err(error):
            assert False

    result = Err("Failure")
    match result:
        case Ok(value):
            assert False
        case Err(error):
            assert error == "Failure"

# Test avec des résultats imbriqués

def test_match_nested_result_ok():
    result = Ok(Ok(42))
    match result:
        case Ok(Ok(value)):
            assert value == 42
        case _:
            assert False

def test_match_nested_result_err():
    result = Ok(Err("Nested Error"))
    match result:
        case Ok(Err(error)):
            assert error == "Nested Error"
        case _:
            assert False
