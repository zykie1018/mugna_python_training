strings = input("Enter string: ").lower().replace(".", "").replace(",", "").replace("?", "")
counts = {}
strings = strings.split(" ")
# "That that is, is. That that is not, is not. Is that it? It is."
for string in strings:
    if string in counts:
        counts[string] += 1
    else:
        counts[string] = 1

print(counts)
