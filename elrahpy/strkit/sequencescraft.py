from elrahpy.strkit.charscraft import check_char_case

def get_all_indexes(seq, element):
    position = []
    for i in range(len(seq)):
        if seq[i] == element:
            position.append(i)
    return position

def remove_all_occurrences(seq, element):
    if isinstance(seq, str):
        return seq.replace(element, "")
    for i in range(len(seq)):
        if i in get_all_indexes(seq, element):
            del [seq[i]]
    return seq



def count_letters(txt: str, sensitive: bool = True):
    txt = txt.lower() if sensitive is False else txt
    letters = {i: txt.count(i) for i in txt}
    return dict(sorted(letters.items()))


def separate_case(txt):
    lw = [i for i in txt if check_char_case(i) == -1]
    up = [i for i in txt if check_char_case(i) == 1]
    return {"lowercase": count_letters(lw), "uppercase": count_letters(up)}
