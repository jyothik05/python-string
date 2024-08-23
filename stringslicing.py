#STRING SLICING
'''
   [n:m]    n = start and m = stop
   *[n:m] returns nth char to to m-1th char (m char is excluded)
   *[:m] slice starts at the begining of the string
   *[n:] slice goes at the end of the string
   *[:] returns total string'''


s = "python"
print(s[:])
print(s[1:5])
print(s[:3])
print(s[2:])
print(s[5:3])


'''
    [start:stop:step]
    step should be always (+ve/-ve) but not be zero '''

str = "programming"
print(str[::-1])
print(str[1:7:2])
print(str[1::3])



#len():returns total no.of chars of a gien string


str = "python programming"
print(len(str))



str2 = 1,2,3,4
print(len(str2))





str = "1234"
print(len(str))

