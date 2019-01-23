import math_func
import pytest

arg_list = [(7, 3, 10), ('Hello', ' World', 'Hello World'),
            (10.5, 25.5, 36.0)]


@pytest.fixture(scope='module')
def db():
    print('=== Setup ===')
    db = math_func.StudentDB()
    db.connect('data.json')
    yield db
    print('=== Tear Down ===')
    db.close()


@pytest.mark.student
def test_scott_data(db):
    db = math_func.StudentDB()
    db.connect('data.json')
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


@pytest.mark.student
def test_mark_data(db):
    db = math_func.StudentDB()
    db.connect('data.json')
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'


@pytest.mark.parametrize('arg1, arg2, result', arg_list)
def test_add(arg1, arg2, result):
    assert math_func.add(arg1, arg2) == result


@pytest.mark.number
def test_multiply():
    assert math_func.multiply(7, 3) == 21
    assert math_func.multiply(7) == 7


@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldolo' not in result


@pytest.mark.strings
def test_multiply_strings():
    result = math_func.multiply('Hello ', 3)
    assert result == 'Hello Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


def test_add_float():
    result = math_func.add(10.5, 25.5)
    assert result == 36
