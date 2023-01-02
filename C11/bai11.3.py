zoo=['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("Danh sách các con thú trong sở thú là ",zoo)
print("Số lượng các con thú trong sở thú là ",len(zoo))
find=input("Nhập con thú cần tìm trong sở thú là: ")
check= find in zoo
if check:
    print(find,'có trong sở thú')
else:
    print(find,'không có trong sở thú')