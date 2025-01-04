l = [ 1, 2, 3 ,4, 5, 6 ,7 ,8 , 9, 10, 11, 12, 13, 14, 15]
element_3 = []
i = 0
while i < 3:
    element_3.append(l[i])
    i += 1
while i:
    element_3.append(l[-i])
    i -= 1

result = element_3[::-1]
print(result)