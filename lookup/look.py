#! /usr/bin/env python

import click
from wordnik import *

API_URL = 'http://api.wordnik.com/v4'


class Look():
    def __init__(self, word, api_key):
        self.word = word
        self.api_key = api_key
        self.api_url = API_URL
        self.client = swagger.ApiClient(self.api_key, self.api_url)
        self.word_api = WordApi.WordApi(self.client)
        self.words_api = WordsApi.WordsApi(self.client)

    def is_valid_word(self):
        defn = self.word_api.getDefinitions(self.word)
        if defn:
            return True
        return False

    def print_defn(self):
        defn = self.word_api.getDefinitions(self.word)
        defn_text = defn[0].text

        click.secho(self.word, fg='green')
        click.secho(defn_text, fg='white')
        print ''

    def print_examples(self):
        example_search_result = self.word_api.getExamples(word=self.word,
                                                          limit=5)

        click.secho('Some examples', fg='blue')

        for example in example_search_result.examples:
            click.secho(example.text, fg='white')

        print ''

    def print_pronunciations(self):
        pronunciations = self.word_api.getTextPronunciations(word=self.word,
                                            limit=5)

        if not pronunciations:
            click.secho('Pronunciation not available', fg='red')
            return
        click.secho('Pronunciation', fg='yellow')

        for pronunciation in pronunciations:
            click.secho(pronunciation.raw, fg='white')

        print ''


def word_of_day(api_key):
    client = swagger.ApiClient(api_key, API_URL)
    words_api = WordsApi.WordsApi(client)

    word_of_day = words_api.getWordOfTheDay()

    click.secho('Word of the day', fg='green')

    print ''
    return word_of_day.word