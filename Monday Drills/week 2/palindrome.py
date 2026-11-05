print("##### PALINDROME #####")

word = input("Enter a word: ").lower()
reverse = ""

for letter in word:
    reverse = letter + reverse

if word == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

## Optional stretch
##print("##### PALINDROME #####")
##
##word = input("Enter a word: ").lower()
##
##palindrome = True
##
##for i in range(len(word) // 2):
##    if word[i] != word[len(word) - 1 - i]:
##        palindrome = False
##        break
##
##if palindrome:
##    print("Palindrome")
##else:
##    print("Not a palindrome")
