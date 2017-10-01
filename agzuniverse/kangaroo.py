#!/bin/python3

def kangaroo(x1, v1, x2, v2):
    if((x1<x2 and v1<=v2) or (x2<x1 and v2<=v1)):
        return("NO")
    elif(x1==x2):
        return("YES")
    elif(x1<x2):
        d1=x1
        d2=x2
        while(d1<d2):
            d1+=v1
            d2+=v2
            if(d1==d2):
                return("YES")
        return("NO")
        
        

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
