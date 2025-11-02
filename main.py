from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters

def main():
    num_words = get_num_words()
    print(f"Found {num_words} total words")
    sort = sort_characters(get_num_characters())
    for char in sort:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char["num"]}")
main()