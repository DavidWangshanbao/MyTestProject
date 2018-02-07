#!/usr/bin/python
#coding=utf-8

import csv

file1 = open('test1.csv', 'rb')
reader = csv.reader(file1)

for line in reader:
    #print line
    for col in line:
        print col,
    print

file1.close()

file2 = open('test2.csv', 'wb')
writer = csv.writer(file2)


writer.writerow([1,2,3,4,5])
writer.writerows([
    [6,7,8],
    [9,10,11,12],
    [13,14,15,16,17]
])
file2.close()