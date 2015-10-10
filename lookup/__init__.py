#! /usr/bin/env python

import os
import argparse

from look import Look
from look import word_of_day

WORDNIK_API_KEY = os.environ.get("WORDNIK_API_KEY")


def is_api_set():
    if WORDNIK_API_KEY is None:
        return False
    return True

def parse_args():
    parser = argparse.ArgumentParser(description='Get the meaning of a word '\
                                     'or get word of day by ignoring options')
    parser.add_argument("-w", "--word", help="Meaning of the word")

    # Optional arguments
    parser.add_argument("-e", "--examples", help="Display with examples",
                        action="store_true")

    parser.add_argument("-p", "--pronounce", help="Get pronunciation",
                        action="store_true")

    args = parser.parse_args()

    # Check if env variable is set
    if not is_api_set():
        print 'Please set WORDNIK_API_KEY env variable \n'
        return

    if not args.word:
        word = word_of_day(WORDNIK_API_KEY)
    else:
        word = args.word

    # Initialize look object
    look = Look(word, WORDNIK_API_KEY)

    # Check if the word is valid
    if not look.is_valid_word():
        print 'Unable to find %s in dictionary' %word
        return

    # Print definition of word by default
    look.print_defn()

    if args.pronounce:
        look.print_pronunciations()

    if args.examples:
        look.print_examples()


def main():
    parse_args()
