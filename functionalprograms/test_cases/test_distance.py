from Utility.utility import dis
import pytest
import json

with open("test.json") as f:
    json_string = json.load(f)
def test_dis():
    x=20
    y=15
    assert dis(x,y) == 25.0

def test_disstring():
    with pytest.raises(TypeError):
        result=dis(json_string['distance'][0]['input1'],json_string['distance'][0]['input2'])
        assert result == json_string['distance'][0]['output']

def test_disspace():
    with pytest.raises(TypeError):
        result=dis(json_string['distance'][1]['input1'],json_string['distance'][1]['input2'])
        assert result == json_string['distance'][1]['output']

def test_disspecial():
    with pytest.raises(TypeError):
        result=dis(json_string['distance'][2]['input1'],json_string['distance'][3]['input2'])
        assert result == json_string['distance'][2]['output']

def test_disinteger():
    with pytest.raises(TypeError):
        result=dis(json_string['distance'][3]['input1'],json_string['distance'][3]['input2'])
        assert result == json_string['distance'][3]['output']
