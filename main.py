def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    word_list = file_contents.split(" ")
    return len(word_list)        

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    num_words = word_count(frankenstein)
    print(f"75767 words found in the document")


main()