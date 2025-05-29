from stats import get_num_words
from stats import get_num_char
from stats import sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    whole_text = get_book_text(book)
    num_words = get_num_words(whole_text)
    num_char = get_num_char(whole_text)
    sorted_num_char = sort_dict(num_char)
    #print(whole_text, num_words, num_char, sorted_num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_num_char:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
        else:
            pass
    print("============= END ===============")

main()
    
