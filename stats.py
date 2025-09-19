def count_words(text):
    words = text.split()
    return len(words)

def character_occurance(text):
    char_count = {}
    for c in text:
        if c.lower() in char_count:
            char_count[c.lower()] += 1
        else:
            char_count[c.lower()] = 1
    return char_count

def dict_to_list_of_dicts(_dict):
    _list = []
    for key, value in _dict.items():
        _list.append({"char": key, "num": value})
    return _list

def sort_on(items):
    return items["num"]