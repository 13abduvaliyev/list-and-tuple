l = list([(1, 3.14, True, "Salom"), (2, False, "Dunyo", 5), (4, 0, "Hello word", False)])
a = 0
new_l = []

for i in l:
    length = len(l[a]) - 1
    
    new_l.append(l[a][length])
    a += 1
    
print(tuple(new_l))