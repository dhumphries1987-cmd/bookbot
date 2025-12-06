def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}

    for ch in text.lower():
        if ch not in char_counts:
            char_counts[ch] = 1
        else:
            char_counts[ch] = char_counts[ch] + 1

    return char_counts

def sort_on(dict):
    return dict["num"]   

def convert_and_sort(char_counts):
    list_of_dicts = []
    for character, count in char_counts.items():
        new_dict = {"char": character, "num": count}
        list_of_dicts.append(new_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)


    return list_of_dicts

   




