#!/usr/bin/env python
'''
My emoji game.
'''
__author__ = "Jaxine Rocha"

import random
import sys
import unicodedata

emoji = chr(random.choice(range(0x1f600, 0x1f64f + 1)))
emoji_name = unicodedata.name(emoji)
print(f"{emoji} ", end="", file=sys.stderr)

tally = 0

try:
    while True:
        guess = input().strip()
        tally += 1

        if guess.casefold() == emoji_name.casefold():
            print(f"Perfect! You got it in {tally} {'tries' if tally > 1 else 'try'}.")
            break

        close = False

        for i in range(len(guess) - 6):
            substring = guess[i:i + 7]
            if substring.lower() in emoji_name.lower():
                close = True
                break
        if close:
            print(
                f"Close enough! You got it in {tally} "
                f"{'tries' if tally > 1 else 'try'}."
                f"The official name is: {emoji_name}.")
            sys.exit()

        print(f"{emoji} ", end="")

except (EOFError, KeyboardInterrupt):
    sys.exit
