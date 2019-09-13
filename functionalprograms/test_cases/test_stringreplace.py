from Utility.utility import strreplace
import pytest
import json

with open("test.json") as f:
    json_string=json.load(f)

def test_strreplace():
    input1="hello user how are you"
    input2="shyam"
    result=strreplace(input1,input2)
    expected="hello shyam how are you"
    assert result == expected

def test_strreplacestring():
    result=strreplace(json_string['strreplace'][0]['input1'],json_string['strreplace'][0]['input2'])
    expected=json_string['strreplace'][0]['output']

def test_strreplacespace():
    result=strreplace(json_string['strreplace'][1]['input1'],json_string['strreplace'][1]['input2'])
    expected=json_string['strreplace'][1]['output']

def test_strreplacespecial():
    result=strreplace(json_string['strreplace'][2]['input1'],json_string['strreplace'][2]['input2'])
    expected=json_string['strreplace'][2]['output']


