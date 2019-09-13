from Utility.utility import fileinsertionsort
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)

def test_fileinsertionsort():
    input=["jettus","thanzeeh","janis","sreeraj","abhi","noothan"]
    result=fileinsertionsort(input)
    expected=["abhi","janis","jettus","noothan","sreeraj","thanzeeh"]
    assert result == expected

def test_fileinsertionsortstring():
    with pytest.raises(TypeError):
        result=fileinsertionsort(json_string['fileinsertionsort'][0]['input'])
        expected = json_string['fileinsertionsort'][0]['output']
        assert result == expected



def test_fileinsertionsortinteger():
    with pytest.raises(TypeError):
        result = fileinsertionsort(json_string['fileinsertionsort'][3]['input'])
        expected = json_string['fileinsertionsort'][3]['output']
        assert result == expected

def test_fileinsertionsortlistinteger():
    result = fileinsertionsort(json_string['fileinsertionsort'][4]['input'])
    expected = json_string['fileinsertionsort'][4]['output']
    assert result == expected
