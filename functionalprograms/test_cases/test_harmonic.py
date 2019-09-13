from Utility.utility import harmonic
import pytest
import json

with open("test.json") as f:
    json_string=json.load(f)

def test_harmonic():
    x=5
    result=harmonic(x)
    assert result == 2.28

def test_harmstring():
    with pytest.raises(TypeError):
        result=harmonic(json_string['harmonic'][0]['input'])
        expected=json_string['harmonic'][0]['output']
        assert result == expected

def test_harmspace():
    with pytest.raises(TypeError):
        result=harmonic(json_string['harmonic'][1]['input'])
        expected=json_string['harmonic'][1]['output']
        assert result == expected

def test_special():
    with pytest.raises(TypeError):
        result=harmonic(json_string['harmonic'][2]['input'])
        expected=json_string['harmonic'][2]['output']
        assert result == expected



def test_harminteger():
    result=harmonic(json_string['harmonic'][3]['input'])
    expected=json_string['harmonic'][3]['output']
    assert result == expected
