from project import parse_args, table, check_format
import pytest



def test_parse_args():
    assert parse_args(['project.py', 'small_list.csv', 'match.csv']) == ('small_list.csv', 'match.csv')
    assert parse_args(['project.py', 'small_list.csv', 'matched.csv']) == ('small_list.csv', 'matched.csv')

    with pytest.raises(SystemExit) as exit:
        parse_args(['project.py'])
        assert exit.type == SystemExit
        assert exit.value.code == 1

def test_table(monkeypatch):
    assert table('matched.csv', 'plain') == True
    assert table('matched.csv', 'simple_grid') == True
    

def test_check_format():
    assert check_format('plain') == 'plain'

    with pytest.raises(SystemExit) as exit:
        parse_args('simple grid')
        assert exit.type == SystemExit
        assert exit.value.code == 1