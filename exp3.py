# -*- coding: utf-8 -*-
"""exp3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gm7xHZveTYSX-Yv4xBtHWauX9VIoIrng
"""

import math
def mean_li(li):
  m=sum(li)/len(li)
  return m
def median_li(li):
  l=sorted(li)
  if(len(l)%2==0):
    ans=(l[len(l)//2]+l[len(l)//2-1])/2
  else:
    ans=l[len(l)//2]
  return ans
def mode_li(li):
  cnt=1
  ans=li[0]
  for i in li:
    if(li.count(i)>cnt):
      cnt=li.count(i)
      ans=i
  return ans
def sd_li(li):
  su=0
  m=sum(li)/len(li)
  for i in li:
    su+=(i-m)*(i-m)
  ans=math.sqrt(su/len(li))
  return ans
li=list (map(int, input(). split()))
print("Mean:",mean_li(li))
print("Median:",median_li(li))
print("Mode:",mode_li(li))
print("Standard Deviation:",sd_li(li))