text = input()

length = len(text)

score = 0
for letter in text:
    if letter == "a":
        score = score + 1
    elif letter == "e":
        score = score + 2
    elif letter == "i":
        score = score + 3
    elif letter == "o":
        score = score + 4
    elif letter == "u":
        score = score + 5

print(score)