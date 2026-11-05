import string
print("##### WORD-FREQUENCY #####")

sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    # Remove punctuation from the beginning and end of the word
    word = word.strip(string.punctuation)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
for word, count in word_count.items():
    print(f"{word}: {count}")
