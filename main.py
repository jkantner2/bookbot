def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = word_count(text)
    count = letter_count(text)
    book_report = report(count)
    book_report.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print_info(book_report)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    word_list = text.split()
    return len(word_list)

def letter_count(text):
    letter_count = {}
    lower_text = text.lower().split()
    temp = []
    for letter in lower_text:
        temp.extend(letter)
    for letter in temp:
        if (letter in letter_count):
            letter_count[letter] += 1
        elif letter.isalpha():
            letter_count[letter] = 1
    return letter_count

def report(dictionary):
    temp = []
    for item in dictionary:
        value = dictionary[item]
        new_dict = {"name": "", "num": ""}
        new_dict["name"] = item
        new_dict["num"] = value
        temp.append(new_dict)
    return temp


def sort_on(dict):
    return dict["num"]

def print_info(report_list):
    for item in report_list:
        letter = item["name"]
        value = item["num"]
        print(f"The {letter} character was found {value} times\n")

main()