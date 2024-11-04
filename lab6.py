import data
from typing import Optional
from data import Book

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def index_smallest_from_book(values:list[Book], start:int) -> Optional[int]:
# Finds the index of the book with the smallest title (lexicographically) in a sublist starting from a given index
# Parameters: values (list[Book]): A list of Book objects, start (int): The starting index to search from
# Returns: Optional[int]: The index of the book with the smallest title after the start index or None if start is out of bounds
    if start >= len(values) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx].title < values[mindex].title:
            mindex = idx
    return mindex

def selection_sort_books(book_list:list[Book]):
# Sorts a list of Book objects in-place by title in ascending order using selection sort
# Parameters: book_list (list[Book]): A list of Book objects
# Returns: list[Book]: The sorted list of Book objects
    for idx in range(len(book_list) - 1):
        mindex = index_smallest_from_book(book_list, idx)
        tmp = book_list[mindex]
        book_list[mindex] = book_list[idx]
        book_list[idx] = tmp
    return book_list
#    book_list.sort(key=lambda x: x.title)
#    return book_list


# Part 2
def swap_case(word:str):
# Reverses the case of each letter in a given word
# Parameters: word (str): The input word whose letters will have their cases swapped
# Returns: str: The word with uppercase letters converted to lowercase and vice versa
    letters = list(word)
    for i in range(len(letters)):
        if letters[i].isupper():
            letters[i] = letters[i].lower()
        elif letters[i].islower():
            letters[i] = letters[i].upper()
    reverse=''.join(letters)
    return reverse
    #letters = word.swapcase()

# Part 3
# Translates a character in a word to another character
# Parameters: word (str): The string to modify,
# char1 (str): The character to replace, char2 (str): The character to replace with
# Returns: str: The modified string with char1 replaced by char2
def str_translate(word,char1,char2):
    letters = list(word)
    for i in range(len(letters)):
        if letters[i]==char1:
            letters[i] = char2
    reverse = ''.join(letters)
    return reverse


# Part 4
# Creates a histogram (frequency dictionary) of words in a sentence
#  Parameters: sentence (str): The sentence to analyze
#  Returns: Dict[str, int]: A dictionary where keys are words and values are the number of occurrences
def histogram(sentence):
    sentence = sentence.split()
    dictionary = {}
    for word in sentence:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
