l = [2, 1, 2, 3, 4, -1, 3]

m = []
for i in l:
    if not i in m: m.append(i)
print(m)

x = 0
for i in l:
    x = x + i
print(x)

n = [l[0], l[0]]
for i in l:
    if i <= n[0]: n[0] = i
    elif i > n[1]: n[1] = i
print(n)