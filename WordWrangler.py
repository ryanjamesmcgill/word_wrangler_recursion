"""
Student code for Word Wrangler game
"""

import urllib2
#import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    singles = []
    
    if (len(list1) > 0):
        singles.append(list1[0])
        for item in list1:
            if (item != singles[-1]):
                singles.append(item)
    return singles

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    intersections = []
    index1 = 0
    index2 = 0
    while(index1 < len(list1) and index2 < len(list2)):
        if (list1[index1] == list2[index2]):
            intersections.append(list1[index1])
            index1 += 1
            index2 += 1
        elif (list1[index1] < list2[index2]):
            index1 += 1
        else:
            index2 += 1
    
    return intersections

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    merges = []
    list1c = list1[:]
    list2c = list2[:]

    while(len(list1c) > 0 and len(list2c) > 0):
        if (list1c[0] == list2c[0]):
            merges.append(list1c.pop(0))
        elif (list1c[0] < list2c[0]):
            merges.append(list1c.pop(0))
        else:
            merges.append(list2c.pop(0))

    merges += list1c + list2c
    
    return merges
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    half1 = []
    half2 = []

    if(len(list1) <= 1):
        return list1

    mid = len(list1) / 2
    half1 = merge_sort(list1[:mid])
    half2 = merge_sort(list1[mid:])

    return merge(half1, half2)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if(len(word)<1):
        return [word]

    first = word[:1]
    rest = word[1:]

    rest_string = gen_all_strings(rest)

    permutations = []

    for string in rest_string:
        for index in range(len(string)+1):
            permutations.append(string[:index] + first + string[index:])

    return rest_string + permutations

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()



    
    
