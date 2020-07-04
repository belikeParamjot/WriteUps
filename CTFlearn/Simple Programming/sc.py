#!/bin/python

with open("data.dat","r") as file:
    count = 0
    for line in file:
        count1,count0 = 0,0
        for i in line:
            if(i=='0'):
                count0+=1
            if(i=='1'):
                count1+=1
        if (count0%3==0) or (count1%2==0):
            count+=1

    print count
