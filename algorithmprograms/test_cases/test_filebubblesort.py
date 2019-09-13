from Utility.utility import bubsort
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)

def test_filebubblesort():
    input=["jettus","thanzeeh","janis","sreeraj","abhi","noothan"]
    result=bubsort(input)
    expected=["abhi","janis","jettus","noothan","sreeraj","thanzeeh"]
    assert result == expected

def test_filebubblesortstring():
    with pytest.raises(TypeError):
        result=bubsort(json_string['filebubblesort'][0]['input'])
        expected = json_string['filebubblesort'][0]['output']
        assert result == expected




def test_filebinaryseachinteger():
    with pytest.raises(TypeError):
        result=bubsort(json_string['filebubblesort'][3]['input'])
        expected = json_string['filebubblesort'][3]['output']
        assert result == expected

def test_filebinaryseachlistinteger():
    result=bubsort(json_string['filebubblesort'][4]['input'])
    expected = json_string['filebubblesort'][4]['output']
    assert result == expected
