from collections import Counter
from common import get_words_from_file


def count_words_in_file(file_name):
    all_words = get_words_from_file(file_name)
    word_statistics = Counter(all_words)

    return word_statistics


if __name__ == '__main__':
    word_stats = count_words_in_file('li.txt')

    for x in word_stats.most_common(10):
        print(x),
