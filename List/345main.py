l = [23, 4, 45, -54, -5456 -56.56, True, False, "Salom"]
l_musbat = []

for i in l:
    if isinstance(i, int) and i > 0:
        l_musbat.append(i)
print(l_musbat)