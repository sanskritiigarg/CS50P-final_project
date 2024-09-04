from project import parse_args, table, check_format
import pytest

def test_parse_args():
    assert parse_args(["project.py", "small_list.csv", "match.csv"]) == ("small_list.csv", "match.csv")
    assert parse_args(["project.py", "small_list.csv", "matched.csv"]) == ("small_list.csv", "matched.csv")

    with pytest.raises(SystemExit) as exit:
        parse_args(["project.py"])
        assert exit.type == SystemExit
        assert exit.value.code == 1

def test_table():
    assert table([['match', 'match_email', 'matched', 'matched_email'], ['Hermione Granger', 'hermionegranger@fiction.books', 'Peeta Mellark', 'peetamellark@fiction.books'], ['Ginny Wealsey', 'ginnyweasley@fiction.books', 'Ronald Weasley', 'ronweasley@fiction.books'], ['Katniss Everdeen', 'katnisseverdeen@fiction.books', 'Harry Potter', 'harrypotter@fiction.books'], ['Gellert Grindelwald', 'gellertgrindelwald@fiction.books', 'Albus Dumbledore', 'albusdumbledore@fiction.books']], 'plain') == True
   
def test_check_format():
    assert check_format('plain') == True
    assert check_format('simple grid') == False

    