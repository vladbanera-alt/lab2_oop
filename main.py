import re
from collections import defaultdict

def process_text():
    try:
        #мій номер залікової книжки
        nzk = 5202

        #обчислення C3 і C17
        C3 = nzk % 3
        C17 = nzk % 17

        print(f"C3 = {C3}")
        print(f"C17 = {C17}")


        if C3 != 0 or C17 != 0:
            print("Цей код реалізує варіант: C3=0 (StringBuilder), C17=0")
            return

        text ="Hello World! World Hello.Word Hi!Hello"


        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        groups = defaultdict(list)

        for sentence in sentences:

            words = re.findall(r'\b\w+\b', sentence.lower())
            word_set = frozenset(words)
            groups[word_set].append(sentence)

        max_group = []
        for group in groups.values():
            if len(group) > len(max_group):
                max_group = group

        print("\nНайбільша кількість речень з однаковими словами:", len(max_group))
        print("Речення:")
        for s in max_group:
            print("-", s)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    process_text()
