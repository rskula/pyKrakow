def dollar(arg0, i):
    if arg0[i] == 's':
        print('$')
    else:
        print(arg0[i])
    i+=1
    if i < len(arg0):
      dollar(arg0, i)
word = input('Podaj $lowo: ')

dollar(word,0)