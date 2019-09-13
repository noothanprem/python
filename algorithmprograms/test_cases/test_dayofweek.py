from Utility.utility import date
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)

def test_dayofweek():
    month=1
    d=15
    year=2019
    result=date(month,d,year)
    expected=2
    assert result == expected

def test_dayofweekstring():
    with pytest.raises(TypeError):
        result=date(json_string['dayofweek'][0]['input1'],json_string['dayofweek'][0]['input2'],json_string['dayofweek'][0]['input3'])
        expected=json_string['dayofweek'][0]['output']
        assert result == expected

def test_dayofweekspace():
    with pytest.raises(TypeError):
        result=date(json_string['dayofweek'][1]['input1'],json_string['dayofweek'][1]['input2'],json_string['dayofweek'][1]['input3'])
        expected=json_string['dayofweek'][1]['output']
        assert result == expected

def test_dayofweekspecial():
    with pytest.raises(TypeError):
        result=date(json_string['dayofweek'][2]['input1'],json_string['dayofweek'][2]['input2'],json_string['dayofweek'][2]['input3'])
        expected=json_string['dayofweek'][2]['output']
        assert result == expected

def test_dayofweekinteger():
    result=date(json_string['dayofweek'][3]['input1'],json_string['dayofweek'][3]['input2'],json_string['dayofweek'][3]['input3'])
    expected=json_string['dayofweek'][3]['output']
    assert result == expected

