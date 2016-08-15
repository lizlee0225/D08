#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
    lst_keys = []
    for key, value in d.items():
    	if value == v:
    		lst_keys += key
    return lst_keys


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
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print(reverse_lookup_new(pledge_histogram, 1))
	print(reverse_lookup_new(pledge_histogram, 9))
	print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
