#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    for c in h:
        print(c, h[c])


def print_hist_new(h):
    for c in sorted(h):
        print(c, h[c])


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
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    new_dict = histogram_new(get_pledge_list())
    print_hist_new(new_dict)

   
if __name__ == '__main__':
    main()
