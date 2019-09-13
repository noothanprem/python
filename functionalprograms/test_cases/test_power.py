from Utility.utility import pow1
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)


def test_pow():
    input=3
    result=pow1(input)
    expected=[1,2,4,8]
    assert result == expected

def test_powstring():
    with pytest.raises(TypeError):
        result=pow1(json_string['power'][0]['input'])
        expected=json_string['power'][0]['output']
        assert result == expected

def test_powspace():
    with pytest.raises(TypeError):
        result=pow1(json_string['power'][1]['input'])
        expected=json_string['power'][1]['output']
        assert result == expected

def test_powspecial():
    with pytest.raises(TypeError):
        result=pow1(json_string['power'][2]['input'])
        expected=json_string['power'][2]['output']
        assert result == expected

def test_powinteger():
    result=pow1(json_string['power'][3]['input'])
    expected=json_string['power'][3]['output']
    assert result == expected