import operator


def words_from_file(fd):
    for line in fd:
        if not line:
            break

        for word in line.split():
            yield word


def strip_words(words):
    for word in words:
        stripped = word.strip()\
            .replace(',', '').replace('.', '').lower()
        if stripped:
            yield stripped


def get_words_from_file(path):
    with open(path, 'r') as fd:
        words = words_from_file(fd)
        for word in strip_words(words):
            yield word


def sort_dict_to_list_map(d):
    for item_map in sorted(d.items(),
                           key=operator.itemgetter(0),
                           reverse=True):
        for x in sorted(item_map[1]):
            yield (item_map[0], x)
