from project import parse_args
import pytest

def test_parse_args():
    assert parse_args(['project.py', 'small_list.csv']) == ('small_list.csv', 'match.csv')
    assert parse_args(['project.py', 'small_list.csv', 'matched.csv']) == ('small_list.csv', 'matched.csv')

    with pytest.raises(SystemExit) as exit:
        parse_args(['project.py'])
        assert exit.type == SystemExit
        assert exit.value.code == 1