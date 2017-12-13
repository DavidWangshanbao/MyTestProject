#!/usr/bin/python
# -*- coding: UTF-8 -*-

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
A = [name.upper() for name in names if len(name) >3]
print  A

strings = ['import', 'is', 'with', 'if', 'file', 'exception']
B = {key: val for val, key in enumerate(strings)}
print B


strings = ['a','is','with','if','file','exception']
C ={len(s) for s in strings}    #有长度相同的会只留一个，这在实际上也非常有用
print C


names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
D = [name for lst in names for name in lst if name.count('e')>=2]  #注意遍历顺序，这是实现的关键
print D

tmp = []
for lst in names:
    for name in lst:
        if name.count('e') >= 2:
            tmp.append(name)

print tmp
