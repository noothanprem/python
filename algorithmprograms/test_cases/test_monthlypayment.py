from Utility.utility import monthlypayment
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)

def test_monthlypayment():
    amount=10000
    years=5
    rate=9
    result=monthlypayment(amount,years,rate)
    expected=208
    assert result == expected

def test_monthlypaymentstring():
    with pytest.raises(TypeError):
        result=monthlypayment(json_string['monthlypayment'][0]['input1'],
                              json_string['monthlypayment'][0]['input2'],
                              json_string['monthlypayment'][0]['input3'])
        expected=json_string['monthlypayment'][0]['output']
        assert result == expected

def test_monthlypaymentspace():
    with pytest.raises(TypeError):
        result=monthlypayment(json_string['monthlypayment'][1]['input1'],
                              json_string['monthlypayment'][1]['input2'],
                              json_string['monthlypayment'][1]['input3'])
        expected=json_string['monthlypayment'][1]['output']
        assert result == expected

def test_monthlypaymentspecial():
    with pytest.raises(TypeError):
        result=monthlypayment(json_string['monthlypayment'][2]['input1'],
                              json_string['monthlypayment'][2]['input2'],
                              json_string['monthlypayment'][2]['input3'])
        expected=json_string['monthlypayment'][2]['output']
        assert result == expected

def test_monthlypaymentinteger():
    result=monthlypayment(json_string['monthlypayment'][3]['input1'],
                            json_string['monthlypayment'][3]['input2'],
                            json_string['monthlypayment'][3]['input3'])
    expected=json_string['monthlypayment'][3]['output']
    assert result == expected