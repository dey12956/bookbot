def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

      

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    num_words = word_count(frankenstein)
    print(f"{num_words} words found in the document")


from stats import word_count
main()