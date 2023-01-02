a=[]
b=1
while b!=0:
    c=int(input('Nhập giá trị:'))
    a+=[c]
    b=int(input('Tiếp tục nhập giá trị?(Nhập 0 để kết thúc):'))
print('List:',a)
def kiem_tra_so_nguyen_to(x):
    check=True
    if (x<2):
        check=False
        return check
    for i in range(2,x):
        if (x%i==0):
           check=False
           break
    return check
c=[]
for x in a:
    check=kiem_tra_so_nguyen_to(x)
    if check:
        c+=[x]
print('Các số nguyên tố trong list:',c)
c=[]
for x in a:
    if x<0:
        c+=[x]
print('Các phần tử âm trong list:',c)
print('Trung bình cộng các phần tử âm trong list:',sum(c)/len(c))
c=[]
for x in a:
    if x>0:
        c+=[x]
print('Các phần tử dương trong list:',c)
print('Trung bình cộng các phần tử dương trong list:',sum(c)/len(c))
print('Giá trị max trong list:',max(a))
print('Giá trị min trong list:',min(a))
a.sort()
print('List sắp theo thứ tự tăng dần:',a)
