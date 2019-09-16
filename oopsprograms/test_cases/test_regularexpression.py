from oopsprograms.regularexpressionmain import Regex
import pytest
import json

with open("test.json") as f:
    json_string=json.load(f)

r1=Regex()
def test_regexnamereplacestring():
    input1=json_string['regularexpressionname'][0]['input1']
    input2=json_string['regularexpressionname'][0]['input2']
    result=r1.namereplace(input1,input2)
    expected=json_string['regularexpressionname'][0]['output']
    assert result == expected

def test_regexnamereplaceinteger():
    with pytest.raises(TypeError):
        input1=json_string['regularexpressionname'][1]['input1']
        input2=json_string['regularexpressionname'][1]['input2']
        result=r1.namereplace(input1,input2)
        expected=json_string['regularexpressionname'][1]['output']
        assert result == expected

def test_regexnamereplacespace():
    with pytest.raises(AssertionError):
        input1=json_string['regularexpressionname'][2]['input1']
        input2=json_string['regularexpressionname'][2]['input2']
        result=r1.namereplace(input1,input2)
        expected=json_string['regularexpressionname'][2]['output']
        assert result == expected

def test_regexnamereplacespecial():
    with pytest.raises(AssertionError):
        input1=json_string['regularexpressionname'][3]['input1']
        input2=json_string['regularexpressionname'][3]['input2']
        result=r1.namereplace(input1,input2)
        expected=json_string['regularexpressionname'][3]['output']
        assert result == expected


def test_regexfullnamereplacestring():
    input1=json_string['regularexpressionfullname'][0]['input1']
    input2=json_string['regularexpressionfullname'][0]['input2']
    result=r1.fullnamereplace(input1,input2)
    expected=json_string['regularexpressionfullname'][0]['output']
    assert result == expected

def test_regexfullnamereplaceinteger():
    with pytest.raises(TypeError):
        input1=json_string['regularexpressionfullname'][1]['input1']
        input2=json_string['regularexpressionfullname'][1]['input2']
        result=r1.fullnamereplace(input1,input2)
        expected=json_string['regularexpressionfullname'][1]['output']
        assert result == expected

def test_regexfullnamereplacespace():
    with pytest.raises(AssertionError):
        input1=json_string['regularexpressionfullname'][2]['input1']
        input2=json_string['regularexpressionfullname'][2]['input2']
        result=r1.fullnamereplace(input1,input2)
        expected=json_string['regularexpressionfullname'][2]['output']
        assert result == expected

def test_regexfullnamereplacespecial():
    with pytest.raises(AssertionError):
        input1=json_string['regularexpressionfullname'][3]['input1']
        input2=json_string['regularexpressionfullname'][3]['input2']
        result=r1.fullnamereplace(input1,input2)
        expected=json_string['regularexpressionfullname'][3]['output']
        assert result == expected


def test_regexnumbernamereplacestring():
    input1=json_string['regularexpressionnumber'][0]['input1']
    input2=json_string['regularexpressionnumber'][0]['input2']
    result=r1.numberreplace(input1,input2)
    expected=json_string['regularexpressionnumber'][0]['output']
    assert result == expected

def test_regexnumberreplaceinteger():
    with pytest.raises(TypeError):
        input1=json_string['regularexpressionnumber'][1]['input1']
        input2=json_string['regularexpressionnumber'][1]['input2']
        result=r1.numberreplace(input1,input2)
        expected=json_string['regularexpressionnumber'][1]['output']
        assert result == expected

def test_regexnumberreplacespace():
    with pytest.raises(AssertionError):
        input1=json_string['regularexpressionnumber'][2]['input1']
        input2=json_string['regularexpressionnumber'][2]['input2']
        result=r1.numberreplace(input1,input2)
        expected=json_string['regularexpressionnumber'][2]['output']
        assert result == expected

def test_regexnumberreplacespecial():
    with pytest.raises(AssertionError):
        input1=json_string['regularexpressionnumber'][3]['input1']
        input2=json_string['regularexpressionnumber'][3]['input2']
        result=r1.numberreplace(input1,input2)
        expected=json_string['regularexpressionnumber'][3]['output']
        assert result == expected


