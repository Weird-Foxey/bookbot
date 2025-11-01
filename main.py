def get_book_text():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text()
    num_words = len(book.split())
    print(f"Found {num_words} total words")

main()

