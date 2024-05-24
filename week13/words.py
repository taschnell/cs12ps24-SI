#!/usr/bin/env python
"""
Practice with generator functions and/or functional programming, using wordnet.sorted.txt as a
bank of categorized words. All functions receiving and producing iterators shall refrain from
aggregating their input or output, and instead use generators and/or `map()` and `filter()`
iterators to efficiently consume input and produce output. Words shall be classified without
regard to case.

>>> sum(1 for _ in adjectives(open('/srv/datasets/joyce-ulysses.txt')))
57467
>>> sum(1 for _ in adverbs(open('/srv/datasets/joyce-ulysses.txt')))
37836
>>> sum(1 for _ in nouns(open('/srv/datasets/joyce-ulysses.txt')))
118446
>>> sum(1 for _ in verbs(open('/srv/datasets/joyce-ulysses.txt')))
43810
"""
__author__ = "A student in CS 12P, someone@jeff.cis.cabrillo.edu"

import itertools  # for _main() and generating permutations
import re  # for tokenizing words
import sys  # for the main block
from typing import Iterator, TextIO  # for type hints

# Consider adding variables here containing info from the WordNet dataset that will be of use in the
# functions below. Use appropriate objects to optimize the speed of your code.
word_dict = {}
with open("/srv/datasets/wordnet.sorted.txt") as word_sort:
    for line in word_sort:
        keys, value, definition = line.split("\t")
        for key in keys.split(";"):
            word_dict[key.lower()] = value


def filter(text: Iterator[str]) -> Iterator[str]:
    pattern = re.compile(r"[A-Za-z'-]+")
    for line in text:
        for match in re.finditer(pattern, line):
            yield match.group(0)


def adjectives(strings: Iterator[str]) -> Iterator[str]:
    """
    Yields all adjectives present in the input strings, in the order encountered.

    :param strings: an iterator that yields strings, e.g. a file object, list[str], tuple[str], etc.
    :yields: all words in each string yielded by `strings`

    >>> list(adjectives(open('/srv/datasets/party.txt')))
    ['final', 'most', 'essential']
    """
    for word in filter(strings):
        if word.lower() in word_dict and word_dict[word.lower()] == "adj":
            yield word.lower()
        else:
            pass


def adverbs(strings: Iterator[str]) -> Iterator[str]:
    """
    Yields all adverbs present in the input strings, in the order encountered.

    :param strings: an iterator that yields strings, e.g. a file object, list[str], tuple[str], etc.
    :yields: all words in each string yielded by `strings`

    >>> list(adverbs(open('/srv/datasets/party.txt')))
    ['most']
    """
    pass  # TODO


def nouns(strings: Iterator[str]) -> Iterator[str]:
    """
    Yields all nouns present in the input strings, in the order encountered.

    :param strings: an iterator that yields strings, e.g. a file object, list[str], tuple[str], etc.
    :yields: all words in each string yielded by `strings`

    >>> list(nouns(open('/srv/datasets/party.txt')))
    ['Party', 'reject', 'evidence', 'eyes', 'It', 'final', 'essential', 'command']
    """
    pass  # TODO


def verbs(strings: Iterator[str]) -> Iterator[str]:
    """
    Yields all verbs present in the input strings, in the order encountered.

    :param strings: an iterator that yields strings, e.g. a file object, list[str], tuple[str], etc.
    :yields: all words in each string yielded by `strings`

    >>> list(verbs(open('/srv/datasets/party.txt')))
    ['Party', 'reject', 'evidence', 'command']
    """
    pass  # TODO


def anagrams(word: str) -> Iterator[str]:
    """
    Yields all arrangements of the characters in `word` that are words, in lowercase, in any order.

    >>> sorted(set(anagrams('TALES')))
    ['lates', 'least', 'slate', 'stael', 'stale', 'steal', 'stela', 'tesla']
    """
    pass  # TODO


def _main(input_file: TextIO, output_file: TextIO):
    """
    Prints to a file a summary of the word counts in a file.

    >>> _main(open('/srv/datasets/joyce-ulysses.txt'), sys.stdout)
    adjectives: 57467
    adverbs: 37836
    nouns: 118446
    verbs: 43810
    """
    # functions_to_test = (adjectives, adverbs, nouns, verbs)
    # input_iterators = itertools.tee(input_file, len(functions_to_test))
    # for (fun, it) in zip(functions_to_test, input_iterators):
    #   print(f'{fun.__name__}: {sum(1 for _ in fun(it))}', file=output_file)
    i = 0
    for _ in adjectives(open("/srv/datasets/joyce-ulysses.txt")):
        print(_)
        i += 1

    print(i)
    print(sum(1 for _ in adjectives(open("/srv/datasets/joyce-ulysses.txt"))))

    # for iterator in filter(input_file):
    #     for word in iterator:
    #         try:
    #             print(word, word_dict[word.lower()])
    #         except:
    #             print(word)


if __name__ == "__main__":
    _main(open("/srv/datasets/joyce-ulysses.txt"), sys.stdout)
