sentence = input("Enter a sentence: ").lower()
clean_sentence = []

for char in sentence:
    if char.isalnum():
        clean_sentence.append(char)

palindrome = True

for i in range(len(clean_sentence) // 2):
   if clean_sentence[i] != clean_sentence[len(clean_sentence) - 1 - i]:
       palindrome = False
       break

if palindrome:
   print("Palindrome")
else:
   print("Not a palindrome")