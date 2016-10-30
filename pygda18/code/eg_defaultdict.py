from collections import defaultdict
from common import get_words_from_file, sort_dict_to_list_map


def count_words_in_file(file_name):
    word_statistics = defaultdict(int)
    all_words = get_words_from_file(file_name)

    # This is our main loop for counting words
    for word in all_words:
        word_statistics[word] += 1

    return word_statistics


def get_word_occurrences(word_stats):
    word_occurrences = defaultdict(list)

    # This is the main loop for matching number of occurence to words
    for word, number in word_stats.items():
        word_occurrences[number].append(word)

    return word_occurrences


if __name__ == '__main__':
    word_stats = count_words_in_file('li.txt')

    word_occurrences = get_word_occurrences(word_stats)
    for i, x in enumerate(sort_dict_to_list_map(word_occurrences)):
        print(x)
        if i >= 10:
            break
