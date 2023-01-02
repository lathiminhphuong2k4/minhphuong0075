#xác định khách có đến dự tiệc muộn hay không?
arrivals=['Adela','Fleda','Owen','May','Mona','Gillbert','Ford']
#name=input("Nhập tên khách hàng: ")
def party_late(arrivals,name):
    Tre_tiec=False
    thutu=int(0)
    for i in range(1,len(arrivals)):
        if name == arrivals[i]:
            thutu=i
            break
    if thutu >=int(len(arrivals)/2) and thutu<len(arrivals)-1:
        Tre_tiec=True
        print(thutu)
    return Tre_tiec
print(party_late(arrivals,name='Gillbert'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))