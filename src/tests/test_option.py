import pytest
import re
from pyresult import Some, None_, Option


def test_is_some_is_none():
    assert Some(10).is_some() is True
    assert Some(10).is_none() is False
    assert None_().is_some() is False
    assert None_().is_none() is True


def test_unwrap():
    assert Some(42).unwrap() == 42
    assert Some(42).unwrap_or(100) == 42
    assert None_().unwrap_or(100) == 100

    with pytest.raises(ValueError, match=re.escape("Called unwrap() on a None")):
        None_().unwrap()


def test_map():
    assert Some(10).map(lambda x: x * 2) == Some(20)
    assert None_().map(lambda x: x * 2) == None_()


def test_and_then():
    assert Some(10).and_then(lambda x: Some(x * 2)) == Some(20)
    assert None_().and_then(lambda x: Some(x * 2)) == None_()


def test_filter():
    assert Some(10).filter(lambda x: x > 5) == Some(10)
    assert Some(10).filter(lambda x: x < 5) == None_()
    assert None_().filter(lambda x: x > 5) == None_()


def test_map_or():
    assert Some(10).map_or(100, lambda x: x * 2) == 20
    assert None_().map_or(100, lambda x: x * 2) == 100


def test_expect():
    assert Some(42).expect("Value expected") == 42

    with pytest.raises(ValueError, match=re.escape("Value expected")):
        None_().expect("Value expected")


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


def test_some_as_string():
    assert str(Some(42)) == "Some(42)"


def test_is_not_some():
    assert Some(42) != None_()


def test_none_as_string():
    assert str(None_()) == "None"
