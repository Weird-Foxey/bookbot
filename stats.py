def get_book_text():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    book = get_book_text()
    return len(book.split())

def get_num_characters():
    characters = {}
    book = get_book_text().lower()
    for char in book:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    sort_list = []
    for char in characters:
        sort_list.append({"char": char, "num": characters[char]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

