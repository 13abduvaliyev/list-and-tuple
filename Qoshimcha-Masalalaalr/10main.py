l = [1, 2, 3.14, "salom", True, "dunyo", 2, 4, False, 4.2]

raqam = []

for i in l:
    if isinstance(i, (int, float)):
        raqam.append(i)

raqam.sort()

print(raqam[len(raqam) - 3:])