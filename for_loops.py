# A for loop excecutes a block of code for each value in a sequence, such as a range, string, or list

# in this case, x is a variable we are creating to reference
# the current value in the loop
for x in range(1,11):
    #range (1,11) gives us numbers 1 to 10
    # the first number is included
    #the last number is where it stops, but it is not included (exclusive)
    print(x)

#range arguements: (start, stop, step)
for x in range(1,10,2):
    print(x)

#print the even numbers from 1 to 10 (inclusive), but I want them all on one line seperated by a space
for x in range(2,11,2):
    print(x, end = " ")

print()
#going backwards:
for x in range(10,0,-1):
    print(x, end = " ")

print()
# alternative way to go backwards:
for x in reversed(range(1,11)):
    print(x, end = " ")

print()
# iterate over something other than a range
# let's try a string
myStr = "AM CMP is a wonderful class!"
for char in myStr:
    print(char)

for char in myStr: 
    print(ord(char)) #printed in ASCII

shift = 3
encoded = ""
for char in myStr:
    asciival = ord(char)
    asciival += shift
    encoded += chr(asciival)
    # print(chr(asciival), end = "")
print(encoded)

decoded = ""
for char in encoded:
    asciival = ord(char)
    asciival -= shift
    decoded += chr(asciival)
print(decoded)

#without looking at Mykits's answer
#how can we keep the number in a range of 0 - 127?

shift = 297334
encoded = ""
for char in myStr:
    ascival = (ord(char) + shift)%128
    encoded += chr(ascival)
print(encoded)

decoded = ""
for char in encoded:
    ascival = (ord(char) - shift) % 128
    decoded += chr(ascival)
print(decoded)