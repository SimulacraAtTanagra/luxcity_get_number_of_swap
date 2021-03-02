# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:54:32 2021

@author: shane
"""
"""
This function accepts two lists of numbers of equal length. 0 or more swaps 
between list items at the same index must be made in order to have both lists
be in ascending numeric order. This program finds that minimum number of swaps.

Created for the game Luxcity. 
"""


from itertools import product
from collections import Counter

def get_number_of_swap(a, b):
    sCharacters ='01'
    thislist=[]
    for aCombination in product(sCharacters, repeat=len(a)):
        thislist.append(aCombination)
    combolist=[]
    combolist2=[]
    for i in thislist:
        thiscombo=[]
        thatcombo=[]
        for ix,x in enumerate(i):
            if x=='1':
                thiscombo.append(a[ix])
                thatcombo.append(b[ix])
            else:
                thiscombo.append(b[ix])
                thatcombo.append(a[ix])
        combolist.append(thiscombo)
        combolist2.append(thatcombo)
    combolist=[''.join([str(y) for y in x]) for x in combolist]
    combolist=list(set(combolist))
    combolist=[[int(x) for x in y] for y in combolist]
    combolist2=[''.join([str(y) for y in x]) for x in combolist2]
    combolist2=list(set(combolist2))
    combolist2=[[int(x) for x in y] for y in combolist2]
    minimum=999
    for i in range(len(combolist)):
        if sorted(combolist[i])==combolist[i] and sorted(combolist2[i])==combolist2[i]:
            if combolist[i]==a or combolist[i]==b:
                x=9999999
            else:
                x=len(list((Counter(combolist[i])- Counter(a)).elements()) )
                y=len(list((Counter(combolist2[i])- Counter(b)).elements()) )
            if x==y and x<minimum:
                minimum=x
    return(minimum)