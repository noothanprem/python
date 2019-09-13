from Utility.utility import sqrt
import pytest
import json

with open("test.json") as f:
    json_string=json.load(f)

def test_squareroot():
    input=25
    result=sqrt(25)
    expected=5
    assert result == expected

def test_squarerootstring():
    with pytest.raises(TypeError):
        result=sqrt(json_string['squareroot'][0]['input'])
        expected=json_string['squareroot'][0]['output']

def test_squarerootspace():
    with pytest.raises(TypeError):
        result=sqrt(json_string['squareroot'][1]['input'])
        expected=json_string['squareroot'][1]['output']

def test_squarerootspecial():
    with pytest.raises(TypeError):
        result=sqrt(json_string['squareroot'][2]['input'])
        expected=json_string['squareroot'][2]['output']

def test_squarerootinteger():
    result=sqrt(json_string['squareroot'][3]['input'])
    expected=json_string['squareroot'][3]['output']