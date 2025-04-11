def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

      

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    num_words = word_count(frankenstein)
    dict_char_count = get_char_count(frankenstein)
    list_dict = list_sort_dict(dict_char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
main()