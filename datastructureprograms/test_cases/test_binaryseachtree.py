from datastructureprograms import binarysearchtree_utility
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)



def test_binarysearchtreestring():
    input=json_string['binarysearchtree'][0]['input']
    result=binarysearchtree_utility.find(input)
    expected=json_string['binarysearchtree'][0]['output']
    assert result == expected

def test_binarysearchtreeinteger():
    input = json_string['binarysearchtree'][1]['input']
    result = binarysearchtree_utility.find(input)
    expected = json_string['binarysearchtree'][1]['output']
    assert result == expected

def test_binarysearchtreespace():
    input = json_string['binarysearchtree'][2]['input']
    result = binarysearchtree_utility.find(input)
    expected = json_string['binarysearchtree'][2]['output']
    assert result == expected

def test_binarysearchtreespecial():
    input = json_string['binarysearchtree'][3]['input']
    result = binarysearchtree_utility.find(input)
    expected = json_string['binarysearchtree'][3]['output']
    assert result == expected