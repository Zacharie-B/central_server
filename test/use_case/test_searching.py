from use_case.searching_files import SearchingFiles

sf = SearchingFiles()


def test_searching_files():
    result = sf.searching_files(['ra'])
    assert result
