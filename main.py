import sys
from stats import get_num_words
from stats import get_char_counts
from stats import convert_and_sort


def main():
    print(sys.argv)

    # 1. Check that we got a path argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # <-- indented so it only runs when not enough args

    # 2. Get the path from sys.argv
    book_path = sys.argv[1]

    # 3. Use book_path
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_chars = convert_and_sort(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # 4. Loop indentation – this should be aligned with the print above
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
