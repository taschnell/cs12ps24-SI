#!/usr/bin/env python
"""
This module offers several functions that leverage the CMUdict dataset to provide IPA and ARPAbet
pronunciations of English words, as well as syllable counts and (optionally) rhyming words.

Remember that you can run doctests via:
`python -m doctest cmudict.py`
`python -m doctest -v cmudict.py`
"""

import re  # for use in the main block
import sys  # for use in the main block

# TODO Load data from files `cmudict.dict` and `arpabet-to-ipa` into objects to which your
# functions will have access. For example, all functions will be able to access dictionary
# `_word_to_ipa` as defined below:
_word_to_ipa = {}

# Load CMUdict dataset
with open("/srv/datasets/cmudict/cmudict.dict", "r") as cmudict_file:
    for line in cmudict_file:
        word, *pronunciations = line.strip().split()
        if len(word) > 2 and word[-2].isdigit():
            _word_to_ipa[last.lower()].append(
                tuple([(phones) for phones in pronunciations])
            )

        else:
            _word_to_ipa[word.lower()] = [
                tuple([(phones) for phones in pronunciations])
            ]
            last = word


_arpabet_to_ipa = {}
with open("/srv/datasets/arpabet-to-ipa", "r") as arpabet_file:
    for line in arpabet_file:
        arpabet, ipa = line.strip().split()
        _arpabet_to_ipa[arpabet] = ipa


def arpabet(word: str) -> set[tuple[str]]:
    """
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
    """
    try:
        return set(_word_to_ipa[word.lower()])
    except:
        return set()


def ipa(word: str) -> set[str]:
    """
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
    """
    return {
        "".join(_arpabet_to_ipa.get(phone, "") for phone in phones)
        for phones in arpabet(word)
    }


def num_syllables(word: str) -> set[int]:
    """
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
    """
    return {
        len([phone for phone in phones if phone[-1].isdigit()])
        for phones in arpabet(word)
    }


# def rhymes(word: str, match_syllable_count: bool = False) -> set[str]:
#     '''
#     Returns the set of words that rhyme with a given word, if available.
#     Words are considered to rhyme if they share identical ARPAbet phoneme patterns
#     from the final stressed phoneme to the end of the word.
#     Calling this function shall not result in opening any data files.

#     :param word: the word in question, case-insensitive
#     :returns: the words that rhyme with `word`

#     >>> sorted(rhymes('college'))
#     ['acknowledge', 'colledge', 'knowledge']
#     >>> sorted(rhymes('partially'))
#     ['harshly', 'impartially', 'parshley']
#     >>> sorted(rhymes('partially', match_syllable_count=True))
#     ['harshly', 'parshley']
#     '''
#     rhyme_words = set()

#     pronunciations_input = _word_to_ipa[word.lower()]
#     pronunciations_stressed_index = 0
#     print(pronunciations_input)
#     for i in range(len(pronunciations_input[0]) - 1, -1, -1):
#             print(i, '1' in pronunciations_input[0][i] or '2' in pronunciations_input[0][i])
#             if '1' in pronunciations_input[0][i] or '2' in pronunciations_input[0][i]:
#                 pronunciations_stressed_index = i
#                 break

#     for potential_rhyme in _word_to_ipa:
#         if potential_rhyme != word:
#             phonemes = _word_to_ipa[potential_rhyme]
#             stressed_index = -1
#             for i in range(len(phonemes[0]) - 1, -1, -1):
#                 if '1' in phonemes[0][i] or '2' in phonemes[0][i]:
#                     stressed_index = i
#                     break
#             found = True
#             #print(stressed_index, phonemes[0])
#             for i,j in zip(range(stressed_index, len(phonemes[0])), range(pronunciations_stressed_index, len(pronunciations_input[0]))):
#                 #print(i,j, phonemes[0][i] != pronunciations_input[0][j], phonemes[0][i],pronunciations_input[0][j] )
#                 if phonemes[0][i] != pronunciations_input[0][j]:
#                     #print(phonemes[i], pronunciations_input[j])
#                     found = False
#                     break

#             if found:
#                 rhyme_words.add(potential_rhyme)

#     return rhyme_words

def _main(input_source):
    """
    Reproduces the output of sample executable `cs12p_cmudict_ipa` given `sys.stdin` as an argument,
    if function `ipa()` works correctly.

    >>> _main(open('/srv/datasets/two-palindromes.txt'))
    hwʌts/wʌts eɪ/ə kaɪæk wɪðaʊt/wɪθaʊt eɪ/ə roʊtɜr?
    """
    for line in input_source:
        for match in re.finditer(r"[\w']+|\W+", line, flags=re.ASCII):
            print(
                (
                    "/".join(sorted(translation))
                    if (translation := ipa(match[0]))
                    else match[0]
                ),
                end="",
            )


if __name__ == "__main__":
    # _main(sys.stdin)
    # print(sorted(rhymes("college")))
    # print("Expected: ['acknowledge', 'colledge', 'knowledge']")

    # print(sorted(rhymes("partially")))
    # print("Expected: ['harshly', 'impartially', 'parshley']")

    # print(sorted(rhymes("partially", match_syllable_count=True)))
    # print("Expected: ['harshly', 'parshley']")

    print()
