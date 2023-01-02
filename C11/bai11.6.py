inch=[74,74,72,72,73,69,69,71,76,71]
m=[]
for x in inch:
    x*=0.0254
    m+=[x]
print('3 chiều cao đầu tiền là:',m[0],m[1],m[2])
print('3 chiều cao cuối cùng là:',m[-1],m[-2],m[-3])
print('Chiều cao trung bình là:',sum(m)/len(m))
print('Chiều cao lớn nhất là:',max(m))
print('Chiều cao nhỏ nhất là:',min(m))
m.sort()
print('Sắp xếp list theo giá trị tăng dần là:',m)
m.reverse()
print('Sắp xếp list theo giá trị giảm đần:',m)