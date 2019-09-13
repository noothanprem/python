from Utility.utility import leap
import json
import pytest

with open("test.json") as f:
    json_string=json.load(f)
def test_leapyear():
    year=2016
    result=leap(year)
    expected=True
    assert result == expected


def test_leapstring():
    with pytest.raises(TypeError):
        result = leap(json_string['leapyear'][0]['input'])
        expected = json_string['leapyear'][0]['output']
        assert result == expected

def test_leapspace():
    with pytest.raises(TypeError):
        result = leap(json_string['leapyear'][1]['input'])
        expected = json_string['leapyear'][1]['output']
        assert result == expected



def test_leapinteger():
    result=leap(json_string['leapyear'][3]['input'])
    expected=json_string['leapyear'][3]['output']
    assert result == expected


