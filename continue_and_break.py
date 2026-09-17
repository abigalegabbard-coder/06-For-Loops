#print the numbers 1 through 20, but skip 13
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

#stop the loop if we hit 13:
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

"""
Write a program that counts from 1 to 50 but skips every number divisible by 5
Write a loop that counts backward from 100 to 0 by tens
Ask the user for a word, and print each letter one at a time using a for loop
"""