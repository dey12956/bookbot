def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

      

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    num_words = word_count(frankenstein)
    dict_char_count = get_char_count(frankenstein)
    print(f"{num_words} words found in the document")
    print(dict_char_count)


from stats import word_count
from stats import get_char_count
main()