t = 1, 2, 3, 4, 5, 6

i = ""
j = 0
for s in t:
    if j == 2 or j == 5:
        i += str(s)
    j += 1

print(i)