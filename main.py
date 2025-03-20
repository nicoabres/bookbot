import sys
from stats import get_num_words, get_num_characters, sort_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
        
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    num_characters = get_num_characters(contents)
    sorted_num_characters = sort_num_characters(num_characters)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {len(num_words)} total words')
    print('--------- Character Count -------')
    for character in sorted_num_characters:
        character_name = character['name']
        character_num = character['num']
        print(f'{character_name}: {character_num}')
    print('============= END ===============')

main()