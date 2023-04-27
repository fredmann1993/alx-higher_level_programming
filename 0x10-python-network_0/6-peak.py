#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted integers
"""


def find_peak(numbr):
    '''
        Finds the peak in a list of numbers
    '''
    length = len(numbr)
    if length == 0:
        return None
    if length == 1:
        return (numbr[0])
    if length == 2:
        return numbr[0] if numbr[0] >= numbr[1] else numbr[1]

    for idx in range(0, length):
        value = numbr[idx]
        if 0 < idx < length-1 and value >= numbr[idx+1] >= numbr[idx-1]:
            return value
        elif idx == 0 and numbr[idx + 1] <= value:
            return value
        elif idx == length - 1 and numbr[idx - 1] <= value:
            return value
    return pick
