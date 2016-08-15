#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = dict()
    for key, value in d.items():
        inverse.setdefault(value, []).append(key)

    return inverse


def print_hist_newest(d):
    count = 1
    for c in sorted(d):
        if c != count:
            while count != c:
                print("{}:".format(count))
                count += 1
        if c == count:
            print("{}: {}".format(c, d[c]))
            count += 1


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
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
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
