"""
Write a program that counts from 1 to 50 but skips every number divisible by 5
Write a loop that counts backward from 100 to 0 by tens
Ask the user for a word, and print each letter one at a time using a for loop
"""

#Not finished
for x in range (1,51,5):
    print(x, end = " ")

print()
for y in range (100, 0, -10):
    print(y, end = " ")

print()
word = input("Enter a word: ").strip().title()
for char in word:
    print(char)