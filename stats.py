def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_chars_count(book_text):
    lowered_text = book_text.lower()
    chars_dict = {}
    for char in lowered_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(chars_dict):
    return chars_dict["count"]

def sort_chars_by_count(chars_dict):
    list_of_chars = []
    for char, count in chars_dict.items():
        list_of_chars.append({"char": char, "count": count})
    list_of_chars.sort(key=sort_on, reverse=True)
    return list_of_chars

def pretty_print_chars(list_of_dicts):
    for char_dict in list_of_dicts:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["count"]}")
