from project import parse_args

def test_parse_args():
    assert parse_args(['project.py', 'small_list.csv']) == ('small_list.csv', 'match.csv')
    assert parse_args(['project.py', 'small_list.csv', 'matched.csv']) == ('small_list.csv', 'matched.csv')
