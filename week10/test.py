#!/usr/bin/env python
'''
This module offers several functions that leverage the CMUdict dataset to provide IPA and ARPAbet
pronunciations of English words, as well as syllable counts and (optionally) rhyming words.

Remember that you can run doctests via:
`python -m doctest cmudict.py`
`python -m doctest -v cmudict.py`
'''

import re  # for use in the main block
import sys  # for use in the main block

# TODO Load data from files `cmudict.dict` and `arpabet-to-ipa` into objects to which your
# functions will have access. For example, all functions will be able to access dictionary
# `_word_to_ipa` as defined below:
_word_to_ipa = {}


def arpabet(word: str) -> set[tuple[str]]:
  '''
  Returns the set of ARPAbet pronunciations of a given word, if available.
  Calling this function shall not result in opening any data files.

  :param word: the word in question, case-insensitive
  :returns: the pronunciations of `word` as tuples of ARPAbet phonemes

  >>> sorted(arpabet('roof'))
  [('R', 'UH1', 'F'), ('R', 'UW1', 'F')]
  >>> sorted(arpabet('ours'))
  [('AA1', 'R', 'Z'), ('AW1', 'ER0', 'Z'), ('AW1', 'R', 'Z')]
  >>> arpabet('cromulent')
  set()
  '''
  pass  # TODO

set(tuple("a","b","C"), tuple(), tuple())

def ipa(word: str) -> set[str]:
  '''
  Returns the set of IPA pronunciations of a given word, if available.
  Calling this function shall not result in opening any data files.

  :param word: the word in question, case-insensitive
  :returns: the pronunciations of `word` as IPA strings

  >>> sorted(ipa('roof'))
  ['ruf', 'rʊf']
  >>> sorted(ipa('ours'))
  ['aʊrz', 'aʊɜrz', 'ɑrz']
  >>> ipa('cromulent')
  set()
  '''
  pass  # TODO


def num_syllables(word: str) -> set[int]:
  '''
  Returns the set of syllable counts of a given word, if available.
  Calling this function shall not result in opening any data files.

  :param word: the word in question, case-insensitive
  :returns: the syllable count(s) of `word`

  >>> num_syllables('roof')
  {1}
  >>> num_syllables('ours')
  {1, 2}
  >>> num_syllables('cromulent')
  set()
  '''
  pass  # TODO


def rhymes(word: str, match_syllable_count: bool = False) -> set[str]:
  '''
  Returns the set of words that rhyme with a given word, if available.
  Words are considered to rhyme if they share identical ARPAbet phoneme patterns
  from the final stressed phoneme to the end of the word.
  Calling this function shall not result in opening any data files.

  :param word: the word in question, case-insensitive
  :returns: the words that rhyme with `word`

  >>> sorted(rhymes('college'))
  ['acknowledge', 'colledge', 'knowledge']
  >>> sorted(rhymes('partially'))
  ['harshly', 'impartially', 'parshley']
  >>> sorted(rhymes('partially', match_syllable_count=True))
  ['harshly', 'parshley']
  '''
  pass  # TODO


def _main(input_source):
  '''
  Reproduces the output of sample executable `cs12p_cmudict_ipa` given `sys.stdin` as an argument,
  if function `ipa()` works correctly.

  >>> _main(open('/srv/datasets/two-palindromes.txt'))
  hwʌts/wʌts eɪ/ə kaɪæk wɪðaʊt/wɪθaʊt eɪ/ə roʊtɜr?
  '''
  for line in input_source:
    for match in re.finditer(r"[\w']+|\W+", line, flags=re.ASCII):
      print('/'.join(sorted(translation)) if (translation := ipa(match[0])) else match[0], end='')


if __name__ == '__main__':
  _main(sys.stdin)

