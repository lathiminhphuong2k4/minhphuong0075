a=[]
b=1
while b!=0:
    c=int(input('Nhập giá trị:'))
    a+=[c]
    b=int(input('Tiếp tục nhập giá trị?(Nhập 0 để kết thúc):'))
x=int(input('Nhập giá trị cần tìm x:'))
print('list:',a)
print('Tổng các giá trị trong list:',len(a))
print('%i xuất hiện %i lần trong list'%(x,a.count(x)))
d=[]
for i in a:
    if x<i:
        d=d+[i]
print('Các số lớn hơn %i trong list:'%(x),d)