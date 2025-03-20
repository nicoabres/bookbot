def get_num_words(contents):
    num_words = contents.split()

    return num_words

def get_num_characters(contents):
    num_words = get_num_words(contents)
    num_characters = {}
    for word in num_words:
        for character in word:
            character = character.lower()
            if character in num_characters.keys():
                num_characters[character] += 1
            else:
                num_characters[character] = 1

    return num_characters

def sort_on(dict):
    return dict["num"]

def sort_num_characters(num_characters):
    list_characters = []

    for character in num_characters:
        list_characters.append({
            "name": character,
            "num": num_characters[character]
        })

    list_characters.sort(reverse=True, key=sort_on)

    return list_characters