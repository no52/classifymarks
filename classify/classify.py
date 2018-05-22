#!/usr/bin/env python3


import sys


def getData(f):
    results = []
    for line in f:
        number, mark = line.strip().split()
        results.append( [number, int(mark)] )
    return results

def thoseInRange(data, lower, upper):
    students = []
    for [number, mark] in data:
        if lower <= mark < upper:
            students.append(number)
    if len(students) is 0: students = ["none"]
    return students


def showRanges(data):
    lower = boundaries[0]
    for upper in boundaries[1:]:
        candidates = thoseInRange(data,lower,upper)
        candidates.sort()
        print("Between %s and %s"%(lower,upper))
        for student in candidates:
            print("  "+student)
        lower=upper

#put this in this block so it doesn't interfere when running tests
if __name__ == '__main__':
	fname = open(sys.argv[1])
	boundaries = list(map(int, sys.argv[2:]))

	data = getData(fname)
	showRanges(data)




