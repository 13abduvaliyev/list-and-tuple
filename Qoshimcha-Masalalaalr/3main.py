l1 = [1, 2.3, "Salom", "Dunyo", False, 5, True]
l2 = []
l2 += l1[::3]

t = tuple(l2)

print(t.index(1))