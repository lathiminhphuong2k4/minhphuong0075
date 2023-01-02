a=()
b=()
for x in range(4):
    a1=int(input('Nhập phần tử '+str(x+1)+' của tuple a:'))
    a+=(a1,)
for x in range(4):
    b1=int(input('Nhập phần tử '+str(x+1)+' của tuple b:'))
    b+=(b1,)
print('Tuple a:',a)
print('Tuple b:',b)
c=a+b
print('Tuple c:',c)
d=tuple(sorted(c))
print('Tuple d:',d)
print('3 phần tử cuối cùng của tuple d',d[-3:])
