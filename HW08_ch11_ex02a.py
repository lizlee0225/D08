#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports


# Body
pledge_histogram = {}


def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_new(s):
    word_count = dict()
    for word in s:
        # Makes words lowercase to count them as same words
        word = word.lower()
        word_count[word] = word_count.get(word,0) + 1
    return word_count



        


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    pledge_list = []
    with open('pledge.txt', 'r') as words:
        for line in words: 
            pledge_list += line.split()
    pledge_list = [word.replace('.',"") for word in pledge_list]



    return pledge_list


###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
