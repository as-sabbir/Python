x=0;
y=1;
for i in range(0,20):
    z=x+y;
    x=y;
    y=z;
    if z>200:
        break;
    print(z);
