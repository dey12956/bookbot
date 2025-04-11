def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

      

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = word_count(book_text)
    dict_char_count = get_char_count(book_text)
    list_dict = list_sort_dict(dict_char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in list_dict:
        if d["char"].isalpha():
            print(str(d["char"])+": "+str(d["num"])+"\n")
    print("============= END ===============")
    

    


from stats import word_count
from stats import get_char_count
from stats import list_sort_dict
import sys
main()