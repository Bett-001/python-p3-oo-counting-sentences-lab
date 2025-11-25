#!/usr/bin/env python3

# class MyString:
#   pass
import re

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        # Replace all sentence-ending punctuation with periods
        cleaned = re.sub(r"[!?.]+", ".", self.value)

        # Split on the periods
        parts = cleaned.split(".")

        # Filter out empty entries or spaces
        sentences = [p.strip() for p in parts if p.strip()]

        return len(sentences)
