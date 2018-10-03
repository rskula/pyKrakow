even = 0
odd = 0

for i in range(100):
    if i % 2 == 0: even += 1
    else: odd +=1
print('Parzyste: {}'.format(even) + f'\nNieparzyste: {odd}')

print('\n-- \n')

# def fib(x):
#     if x == 0: return 0
#     elif x == 1: return 1
#     else:
#         return (fib(x-1) + fib(x-2))
myfib = {0:0, 1:1}
def fib(x):
    if not x in myfib: myfib[x] = fib(x-1) + fib(x-2)
    return myfib[x]
fibi=0
dofib=fib(fibi)
while dofib < 100:
    fibi +=1
    print(dofib)
    dofib = fib(fibi)

print('\n-- \n')

a, b = 0, 1
print(a)
print(b)
while a + b < 100:
    c = a + b
    a = b
    b = c
    print(c)

print('\n-- \n')

strong = 1
for i in range(5):
    strong = strong * (i+1)
print(strong)