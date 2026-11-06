import string

def longest_word(sentence): 
    longest = ""

    for word in sentence.split():
        word = word.strip(string.punctuation)

        if not word:
            continue

        if len(word) > len(longest):
            longest = word

    return longest

# bonus
import string

def longest_words(sentence): 
    words = [ word.strip(string.punctuation) for word in sentence.split() if word.strip(string.punctuation) ]

    if not words:
        return []

    longest = max(len(word) for word in words)

    return [word for word in words if len(word) == longest]