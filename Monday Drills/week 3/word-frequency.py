"""
START

INPUT the paragraph

CONVERT the paragraph to lowercase

SET punctuation = ",.!?;:'\"-"
SET cleaned_text = empty string

FOR each character in the paragraph:

    IF character is in punctuation:
        REPLACE character with a space
    ELSE:
        ADD character to cleaned_text

SPLIT cleaned_text into individual words

CREATE an empty dictionary called word_counts

FOR each word:

    IF word already exists in word_counts:
        INCREASE its count by 1
    ELSE:
        SET its count to 1

SET most_frequent_word = nothing
SET highest_count = 0

FOR each word in word_counts:

    IF word_counts[word] > highest_count:
        SET highest_count = word_counts[word]
        SET most_frequent_word = word

PRINT most_frequent_word and highest_count

END
"""
paragraph = input("Enter a paragraph: ")

paragraph = paragraph.lower()

punctuation = ",.!?;:'\"-"
cleaned_text = ""

for character in paragraph:
    if character in punctuation:
        continue
    else:
        cleaned_text += character

words = cleaned_text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_frequent_word = None
highest_count = 0

for word in word_counts:
    if word_counts[word] > highest_count:
        highest_count = word_counts[word]
        most_frequent_word = word

print(f"Most frequent word: {most_frequent_word} ({highest_count})")