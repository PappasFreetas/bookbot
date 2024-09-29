def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    num_words = count_words(text)
    # print(num_words)
    num_chars_dict = count_chars(text)
    # print(num_chars_dict)
    list_of_char_dicts = convert_dict_to_list(num_chars_dict)
    list_of_char_dicts.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document")
    printlist(list_of_char_dicts)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    counter = 0
    words = text.split()
    for word in words: # Can also jut do len(words)
        counter +=1    # instead of this loop
    return counter

def count_chars(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def convert_dict_to_list(dict):
    rtn_list = []
    for letter in dict:
        if not letter.isalpha():
            continue
        num = dict[letter]
        rtn_list.append({"letter":letter,"num":num})
    return rtn_list

def sort_on(dict):
    return dict["num"]

def printlist(list):
    for item in list:
        print(f"The '{item["letter"]}' character was found {item["num"]} times")


main()