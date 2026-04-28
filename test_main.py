import pytest
from main import (
    calculate_c_values,
    split_into_sentences,
    normalize_sentence,
    find_max_sentences_with_same_words
)


def test_calculate_c_values():
    c3, c17 = calculate_c_values(5202)
    assert c3 == 0
    assert c17 == 0


def test_split_into_sentences():
    text = "Alpha beta! Gamma delta. Epsilon zeta?"
    result = split_into_sentences(text)

    assert result == [
        "Alpha beta",
        "Gamma delta",
        "Epsilon zeta"
    ]


def test_normalize_sentence_case_insensitive():
    s1 = normalize_sentence("Orange Apple")
    s2 = normalize_sentence("apple orange")

    assert s1 == s2


def test_normalize_sentence_punctuation():
    s = normalize_sentence("Rocket, planet!!!")
    assert s == {"rocket", "planet"}


def test_find_max_sentences_basic():
    text = "Red blue! Blue red. Yellow green."
    result = find_max_sentences_with_same_words(text)

    assert len(result) == 2


def test_find_max_sentences_no_duplicates():
    text = "One alpha. Two beta. Three gamma."
    result = find_max_sentences_with_same_words(text)

    assert len(result) == 1


def test_find_max_sentences_empty():
    text = ""
    result = find_max_sentences_with_same_words(text)

    assert result == []


def test_find_max_sentences_case_insensitive():
    text = "Sky cloud! cloud sky! SKY CLOUD!"
    result = find_max_sentences_with_same_words(text)

    assert len(result) == 3


def test_find_max_sentences_complex():
    text = (
        "Stone river. River stone! Fire water. "
        "Water fire. Stone river."
    )
    result = find_max_sentences_with_same_words(text)

    assert len(result) == 3
