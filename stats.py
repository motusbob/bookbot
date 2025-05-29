def get_num_words(text):
    return (len(text.split()))

def get_num_char(text):
    char_count = {}
    for word in text.split():
        for c in word:
            if c.lower() in char_count:
                char_count[c.lower()] += 1
            else:
                char_count[c.lower()] = 1
    return char_count

def sort_on(dict):
    return(dict["num"])

def sort_dict(char_dict):
    dict_list = []
    for key in char_dict:
        this_dict = {}
        this_dict = {"char": key, "num" : char_dict[key]}
        dict_list.append(this_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list 
