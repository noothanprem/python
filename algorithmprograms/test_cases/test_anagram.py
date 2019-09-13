from Utility.utility import checkanagram
import pytest
import json

with open("test.json") as f:
    json_string=json.load(f)


def test_anagram():
    input1="mad"
    input2="adm"
    result=checkanagram(input1,input2)
    expected=True
    assert result == expected


def test_anagramstring():
    result=checkanagram(json_string['anagram'][0]['input1'],json_string['anagram'][0]['input2'])
    expected=json_string['anagram'][0]['output']
    assert result == expected

def test_anagramspace():
    result=checkanagram(json_string['anagram'][1]['input1'],json_string['anagram'][1]['input2'])
    expected=json_string['anagram'][1]['output']
    assert result == expected

def test_anagramspecial():
    result=checkanagram(json_string['anagram'][2]['input1'],json_string['anagram'][2]['input2'])
    expected=json_string['anagram'][2]['output']
    assert result == expected

def test_anagraminteger():
    with pytest.raises(TypeError):
        result=checkanagram(json_string['anagram'][3]['input1'],json_string['anagram'][3]['input2'])
        expected=json_string['anagram'][3]['output']
        assert result == expected