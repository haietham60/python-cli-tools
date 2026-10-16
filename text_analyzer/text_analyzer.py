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


def most_common_word(text: str) -> list[tuple[str, int]]:
    words = text.lower().split()
    if not words:
        return []
    counter: dict[str, int] = {}
    for word in words:
        word = word.strip(".,!?;:()[]{}\"'")
        if word:
            counter[word] = counter.get(word, 0) + 1
    sorted_words = sorted(
        counter.items(),
        key=lambda item: item[1],
        reverse=True
    )
    top_five = sorted_words[:5]
    if not counter:
        return []

    return top_five


def display_results(
    characters: int,
    words: int,
    lines: int,
    common_word: list[tuple[str, int]]
) -> None:
    print("=" * 30)
    print("        Text Analyzer")
    print("=" * 30)
    print()
    print(f"Characters       : {characters}")
    print(f"Words            : {words}")
    print(f"Lines            : {lines}")
    print()
    print("Top 5 words      :")
    for word, count in common_word:
        print(f"  {word:<15}: {count}")
    print()
    print("=" * 30)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Need one argument")
    else:
        if sys.argv[1] == "--file":
            if len(sys.argv) < 3:
                print("Need files name")
                sys.exit(1)
            try:
                with open(sys.argv[2], 'r', encoding='utf-8') as files:
                    text = files.read()
            except FileNotFoundError as e:
                print(e)
                sys.exit(1)
            except PermissionError as e:
                print(e)
                sys.exit(1)
        elif sys.argv[1].startswith("--"):
            print("Unknown option")
            sys.exit(1)
        else:
            text = " ".join(sys.argv[1:])
        characters = count_characters(text)
        words = count_words(text)
        lines = count_lines(text)
        common_word = most_common_word(text)
        display_results(characters, words, lines, common_word)
