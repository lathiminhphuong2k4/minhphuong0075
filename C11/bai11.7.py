def elementwise_greater_than(L,thresh):
    a=[]
    for i in L:
        if i>thresh:
            a+=[True]
        else:
            a+=[False]
    return a
L=[1,2,3,4]
thresh=2
print(elementwise_greater_than(L,thresh))
