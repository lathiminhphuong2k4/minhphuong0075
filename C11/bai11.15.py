tudien={'cat':'con mèo','dog':'con chó','ant':'con kiến','bear':'con gấu'}
while True:
    a=int(input('Bạn muốn làm gì? 1:xem từ điển; 2:Tra từ; 3:Thêm từ; 4:Xóa từ'))
    if a==1:
        print('Dictionary: ')
        print('{:<50} {:20}'.format('Từ Anh','Nghĩa Việt'))
        for key,Value in tudien.items():
            print('{:<50}{:20}'.format(key,Value))
    elif a==2:
        timkiem=input('Nhập từ cần tra: ')
        nghiaviet=tudien.get(timkiem)
        if nghiaviet == None:
            print('Không tìm thấy: ')
            
