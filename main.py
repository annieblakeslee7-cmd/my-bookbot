"""
from stats import get_word_count
from stats import get_char_count
"""
import sys
from stats import *



def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def print_report(book_text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(word_count)
    print("--------- Character Count -------")
    char_count = get_char_count(book_text)
    sorted_char_count = chars_dict_to_sorted_list(char_count)
    report_list = [f"{char}: {count}" for char, count in sorted_char_count if char.isalpha()]
    print("\n".join(report_list))
    print("============= END ===============")

def main():
    print("Welcome to BookBot! To run this program, please use python3 main.py <path_to_book>")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    print_report(book_text)
    

main()