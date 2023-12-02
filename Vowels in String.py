string = input().upper()
vowels = 0
for i in range(len(string)):
    if string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U":
        vowels += 1
print(vowels)