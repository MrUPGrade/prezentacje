from common import get_words_from_file, sort_dict_to_list_map


def count_words_in_file(file_name):
    word_statistics = {}
    all_words = get_words_from_file(file_name)

    # This is our main loop for counting words
    for word in all_words:
        try:
            word_count = word_statistics[word]
        except KeyError:
            word_count = 0

        word_count += 1
        word_statistics[word] = word_count

    return word_statistics


def get_word_occurrences(word_stats):
    word_occurrences = {}

    # This is the main loop for matching number of occurence to words
    for word, number in word_stats.items():
        try:
            word_list = word_occurrences[number]
        except KeyError:
            word_list = []
            word_occurrences[number] = word_list

        word_list.append(word)

    return word_occurrences


if __name__ == '__main__':
    word_stats = count_words_in_file('li.txt')

    word_occurrences = get_word_occurrences(word_stats)

    for i, x in enumerate(sort_dict_to_list_map(word_occurrences)):
        print(x)
        if i >= 10:
            break
