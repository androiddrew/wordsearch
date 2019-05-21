from wordsearch.app import WordIndex


def test_create_word_index():
    w = WordIndex(words=["apple", "banana"])
    assert w.index["a"] == ["apple"]


def test_add_words_to_index():
    w = WordIndex(words=["apple", "banana"])
    w.add_word("Animal")
    w.add_word("data")
    print(w.index["a"])
    assert "animal" in w.index["a"]
    assert "data" in w.index["d"]


def test_word_index_sort():
    w = WordIndex(words=["apple", "banana"])
    w.add_word("Animal")
    assert w.index["a"] == ["apple", "animal"]
    w.sort_index()
    assert w.index["a"] == ["animal", "apple"]


def test_create_word_index_from_file():
    path = "./words.txt"
    w = WordIndex.from_file(path)
    assert isinstance(w, WordIndex)
    assert "abate" in w.index["a"]
