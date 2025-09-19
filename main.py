import sys
from stats import count_words, character_occurance, dict_to_list_of_dicts, sort_on

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_occ = character_occurance(book_text)
    list_dict = dict_to_list_of_dicts(char_occ)
    list_dict.sort(reverse=True, key=sort_on)
    for items in list_dict:
        if items["char"].isalpha():
            print(f"{items["char"]}: {items["num"]}")
                
    print("============= END ===============")

if __name__ == "__main__":
    main()