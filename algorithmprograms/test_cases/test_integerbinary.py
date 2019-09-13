from Utility.utility import binarysearch
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)

def test_integerbinarysearch():
    input1=5
    input2=[23,67,12,90,54]
    input3=67
    result=binarysearch(input1,input2,input3)
    expected=3
    assert result == expected

def test_integerbinaryseachstring():
    result=binarysearch(json_string['integerbinarysearch'][0]['input1'],json_string['integerbinarysearch'][0]['input2'],json_string['integerbinarysearch'][0]['input3'])
    expected = json_string['integerbinarysearch'][0]['output']
    assert result == expected

def test_integerbinaryseachspace():
    result = binarysearch(json_string['integerbinarysearch'][1]['input1'],
                          json_string['integerbinarysearch'][1]['input2'],
                          json_string['integerbinarysearch'][1]['input3'])
    expected = json_string['integerbinarysearch'][1]['output']
    assert result == expected


def test_integerbinaryseachspecial():
    result = binarysearch(json_string['integerbinarysearch'][2]['input1'],
                          json_string['integerbinarysearch'][2]['input2'],
                          json_string['integerbinarysearch'][2]['input3'])
    expected = json_string['integerbinarysearch'][2]['output']
    assert result == expected


def test_integerbinaryseachinteger():
    result = binarysearch(json_string['integerbinarysearch'][3]['input1'],
                          json_string['integerbinarysearch'][3]['input2'],
                          json_string['integerbinarysearch'][3]['input3'])
    expected = json_string['integerbinarysearch'][3]['output']
    assert result == expected


def test_integerbinaryseachcorrectinput():
    result = binarysearch(json_string['integerbinarysearch'][4]['input1'],
                          json_string['integerbinarysearch'][4]['input2'],
                          json_string['integerbinarysearch'][4]['input3'])
    expected = json_string['integerbinarysearch'][4]['output']
    assert result == expected
