# #🟡 3. Strings — Exercises 11–20

#🔴 11. String Length - Ask for a word and find its length.
word = input("Enter a word: ")
print(len(word))

#🔴 12. Uppercase - Convert a string to uppercase.
#By using, mystring varible in this conversion.
mystring = input("Enter a string: ")
print(f"This is upper case:", mystring.upper())

#🔴 13. Lowercase - Convert a string to lowercase.
#By using, mystring varible in this conversion.
print(f"This is lower case:", mystring.lower())

#🔴 14. First and Last Character -Print the first and last character of a string.
#By using, mystring varible in this conversion.
print(f"This is first character:", mystring[0])
print(f"This is last character:", mystring[-1])

#🔴 15. Reverse a String - Reverse a string without using a built-in reverse function.
# By using, mystring varible in this conversion.
print(f"This is reverse string:", mystring[::-1])

#🔴 16. Count Vowel - Count how many vowels are in a string.
mytext = input("Enter your string: ")
check_vowel = mytext.count("a") + mytext.count("e") + mytext.count("i") + mytext.count("o") \
    + mytext.count("u")
print(f"The Total Vowels are in this string: {check_vowel}")

#🔴 17. Count Spaces - Count the number of spaces in a sentence.
#By using, mytext varible in this conversion.
spaces = mytext.count(" ")
print(f"The Total spaces in this string are: {spaces}")

#🔴 18. Count a Character - Ask for a string and a character and count how many times that character appears.
yourstring = input("Enter your string: ")
character = input(f"Enter your desire char in: {yourstring}")
check_char = yourstring.count(character)
print(f"This character appears {check_char} many time in this string.")

#🔴 19. Palindrome-Check whether a word is a palindrome.- Example:madam → Palindrome -hello → Not palindrome
word = input("Enter the word: ")
palindrome = word[::-1]
print(f"This word {word == palindrome} is palindrome")

# #🔴 20. Word Counter -Ask the user for a sentence and count how many words it contains.
mysentence = input("Enter the sentence: ")
count_sent = mysentence.count(" ") + 1
print(f"The Total word in this sentence is {count_sent}")



