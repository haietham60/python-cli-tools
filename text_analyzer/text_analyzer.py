import sys


def count_characters(text: str) -> int:
    count = len(text)
    return count


def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_lines(text: str) -> int:
    if not text:
        return 0
    return len(text.splitlines())


def most_common_word(text: str) -> str | None:
    words = text.lower().split()
    if not words:
        return None
    counter: dict[str, int] = {}

    for word in words:
        word = word.strip(".,!?;:()[]{}\"'")
        if word:
            counter[word] = counter.get(word, 0) + 1

    if not counter:
        return None

    return max(counter, key=lambda word: counter[word])


def display_results(
    characters: int,
    words: int,
    lines: int,
    common_word: str | None
) -> None:
    print("=" * 30)
    print("        Text Analyzer")
    print("=" * 30)
    print()
    print(f"Characters       : {characters}")
    print(f"Words            : {words}")
    print(f"Lines            : {lines}")
    print(f"Most common word : {common_word if common_word else 'None'}")
    print()
    print("=" * 30)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Need one argument")
    else:
        text = sys.argv[1]
        characters = count_characters(text)
        words = count_words(text)
        lines = count_lines(text)
        common_word = most_common_word(text)

        display_results(characters, words, lines, common_word)
