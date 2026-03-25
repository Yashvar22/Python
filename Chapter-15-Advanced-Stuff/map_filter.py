#mapping

a=[1,2,3,4,5];

def double(x):
    return 2*x;

res=map(double,a);
doubled=map(lambda x:x*2,a)

print(list(doubled))



#filter

def even(x):
    if x%2==0:
        return True;
    else:
        return False;

a=[1,2,3,4,5,6,7,8,9];

res2=filter(even,a);

print(list(res2))




