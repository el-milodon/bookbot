def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_nr_words(text)
    chars_dict = get_chars_dict(text)
    print(f"--- Begin report of books/frankenstein.txt ---\n{count_words} words found in the document\n")
    for char, count in chars_dict.items():
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_nr_words(text):
    words = text.split()
    count_words = len(words)
    return count_words

def get_unique_chars(low_text):
    unique_chars_set = set(low_text)
    return unique_chars_set

def sorted_dict(my_dict):
    sorted_string = sorted(my_dict.items(), key=lambda x:x[1], reverse = True)
    sorted_dict = dict(sorted_string)
    return sorted_dict

def get_chars_dict(text):
    chars_dict = {}
    low_text = text.lower()
    unique_chars = get_unique_chars(low_text)
    for char in unique_chars:
        if char.isalpha():
            chars_dict[char] = low_text.count(char)
    return sorted_dict(chars_dict)
   
main()