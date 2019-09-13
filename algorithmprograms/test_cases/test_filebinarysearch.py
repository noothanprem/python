from Utility.utility import binary
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)

def test_filebinarysearch():
    input1=['abhi', 'janis', 'jettus', 'noothan', 'sreeraj', 'thanzeeh']
    input2="jettus"
    result=binary(input1,input2)
    expected=2
    assert result == expected

def test_filebinaryseachstring():
    result=binary(json_string['filebinarysearch'][0]['input1'],json_string['filebinarysearch'][0]['input2'])
    expected = json_string['filebinarysearch'][0]['output']
    assert result == expected

def test_filebinaryseachspace():
    result=binary(json_string['filebinarysearch'][1]['input1'],json_string['filebinarysearch'][1]['input2'])
    expected = json_string['filebinarysearch'][1]['output']
    assert result == expected

def test_filebinaryseachspecial():
    result=binary(json_string['filebinarysearch'][2]['input1'],json_string['filebinarysearch'][2]['input2'])
    expected = json_string['filebinarysearch'][2]['output']
    assert result == expected

def test_filebinaryseachinteger():
    with pytest.raises(TypeError):
        result=binary(json_string['filebinarysearch'][3]['input1'],json_string['filebinarysearch'][3]['input2'])
        expected = json_string['filebinarysearch'][3]['output']
        assert result == expected

def test_filebinaryseachlistinteger():
    result=binary(json_string['filebinarysearch'][4]['input1'],json_string['filebinarysearch'][4]['input2'])
    expected = json_string['filebinarysearch'][4]['output']
    assert result == expected
