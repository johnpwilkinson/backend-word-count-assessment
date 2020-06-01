#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "John Wilkinson, youtube, Canvas lessons, and the internet at large"

import sys


def create_word_dict(filename):
    # Doing the reading of the file in the helper function, so that 
    # the other functions are only reposnsible for sorting
    word_dict = {}
    with open(filename, "r") as f:
        for row in f:
            words = row.split()
            for word in words:
                # lower case every word
                to_lower = word.lower()
                if to_lower in word_dict:
                    # if word is in dict all ready, then add 1 to its value (count)
                    word_dict[to_lower] += 1
                else:
                    # if not, then set that words (key) value to 1
                    word_dict[to_lower] = 1
    return word_dict

    


def print_words(filename):
    # call prior formula on txt file passed in terminal
    result = create_word_dict(filename)
    # sort results key value pairs in alphabetical order
    abc_result = sorted(result.items(), key=lambda x: x[0])
    for i in abc_result:
        # print key : value
	    print(f'{i[0]} : {i[1]}')



def print_top(filename):
    # call prior formula on txt file passed in terminal
    result = create_word_dict(filename)
    # sort results by descending value of the value in each key/value pair
    abc_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # get top 20 results
    top_20 = abc_result[:20]
    for i in top_20:
        print(f'{i[0]} : {i[1]}')
    


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
