from datastructureprograms.balancedparantheses import Balanced
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)




def test_balancedstring():
    expr=json_string['balancedparenthesis'][0]['input']
    result=Balanced.check(expr)
    expected=json_string['balancedparenthesis'][0]['output']
    assert result == expected

def test_balancedinteger():
    expr=json_string['balancedparenthesis'][1]['input']
    result=Balanced.check(expr)
    expected=json_string['balancedparenthesis'][1]['output']
    assert result == expected

def test_balancedspace():
    expr = json_string['balancedparenthesis'][2]['input']
    result = Balanced.check(expr)
    expected = json_string['balancedparenthesis'][2]['output']
    assert result == expected

def test_balancedspecial():
    expr = json_string['balancedparenthesis'][3]['input']
    result = Balanced.check(expr)
    expected = json_string['balancedparenthesis'][3]['output']
    assert result == expected