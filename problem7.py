#import math;
#print(math.gcd(48,60));

def myfunction(x,y):
    if x<y:
        small=x;
    else:
        small=y;
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            gcd=i;
    return gcd;
print(myfunction(48,60));
