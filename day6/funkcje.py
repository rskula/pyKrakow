# def foo(a, l=None):
#     if not l: l=[]
#     l.append(a)
#     print(l)
#
# foo(1)
# foo(2)
# foo(3)
# foo(4)

def my_max(a=0, b=0):
    if a >= b: return a
    return b

# print(my_max(10,2))

random_list = [5, 4, 7, 2, 7, 14, 2, 5, 14, 3, 8, 4, 6, 2, 8]

x = random_list[0]
for i in random_list:
    if my_max(x, i) == i: x = i

print(x)