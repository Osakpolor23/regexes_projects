import re
import sys


def main():
    text = input("Text: ")
    print(count(text))


def count(text):
    return len(re.findall(r"\bum\b", text, re.IGNORECASE))   # re.findall() returns a list of the matches.
                                                             # the len() captures the number of items in the list.
                                                             # \b placed before and after a word defines the between the word
                                                             # and ensures only the matches of that word standing alone is captured e.g um, hello.
                                                             # and not as a substring within a text e.g yummy
    

if __name__ == "__main__":
    main()