f = open("text.txt", "r")

text = []
for line in f:
    words = line.split()
    for word in words:
      text.append(word)

f.close()

text.sort()
fixedText = list(dict.fromkeys(text))

print(fixedText)