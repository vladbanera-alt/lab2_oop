import re
from collections import defaultdict


def calculate_c_values(nzk: int):
    c3 = nzk % 3
    c17 = nzk % 17
    return c3, c17


def split_into_sentences(text: str):

    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]


def normalize_sentence(sentence: str):

    words = re.findall(r'\b\w+\b', sentence.lower())
    return frozenset(words)


def find_max_sentences_with_same_words(text: str):

    if not text or not text.strip():
        return []

    sentences = split_into_sentences(text)
    groups = defaultdict(list)

    for sentence in sentences:
        word_set = normalize_sentence(sentence)
        groups[word_set].append(sentence)

    max_group = []
    for group in groups.values():
        if len(group) > len(max_group):
            max_group = group

    return max_group


def main():
    
    try:
        record_book_number = 5202

        text = (
            "Hello world! "
            "World hello. "
            "Hi World "
            "Test Hello World"
            "Word Helo"
        )

        c3, c17 = calculate_c_values(record_book_number)

        print(f"C3 = {c3}")
        print(f"C17 = {c17}")

        if c3 != 0 or c17 != 0:
            print("Ця програма реалізує варіант: C3 = 0, C17 = 0")
            return

        result = find_max_sentences_with_same_words(text)

        print("\nРезультат:")
        print("Кількість речень:", len(result))

        for i, sentence in enumerate(result, 1):
            print(f"{i}. {sentence}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
