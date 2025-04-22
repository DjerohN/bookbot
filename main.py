import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_chars_count
from stats import sort_chars_by_count
from stats import pretty_print_chars

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(args[1])
    word_count = get_word_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    chars_dict = get_chars_count(book_text)
    sorted_chars = sort_chars_by_count(chars_dict)
    print("--------- Character Count -------")
    pretty_print_chars(sorted_chars)
    print("============= END ===============")

main()
