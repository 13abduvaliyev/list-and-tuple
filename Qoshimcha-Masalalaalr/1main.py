l = [1, 6, "Salom", True, 5.5, 3, "Dunyo"]


new_l = []
for element in l:
    if type(element) == str:
        new_l.append(element.upper())
    else:
        new_l.append(element)

print(new_l)