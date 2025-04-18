def word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)  

def get_char_count(file_contents):
    file_contents = file_contents.lower()
    dict_char_count = {}
    for char in file_contents:
        if char in dict_char_count:
            dict_char_count[char] += 1
        else:
            dict_char_count[char] = 1
    return dict_char_count

def list_sort_dict(dict_char_count):
    dict_list = []
    for k, v in dict_char_count.items():
        new_dict = {"char": k, "num": v}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key = lambda d:d["num"])
    return dict_list