from stats import get_num_words
from stats import get_num_characters

def main():
    num_words = get_num_words()
    print(f"Found {num_words} total words")
    print(get_num_characters())

main()