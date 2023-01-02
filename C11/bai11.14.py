danhba ={}
danhba = {'0989741258':"Minh",'0903852147':"Hạnh",'0913753951':"Bình",'0933753654':"An"}
def in_danhba(danhba):
    for i in danhba:
        print('Số điện thoại',i,":",danhba[i])
def tim_kiem(danhba):
    ten=input("Nhập tên cần tìm :")
    flag=False
    for key , value in danhba.items():
        if ten==value:
            print(value,'Có số điện thoại là: %s'%key)
            flag=True
            break
        if flag==False:
            print('%s Chưa có số điện thoại'%(ten))
def them_moi(danhba):
    ten=input('Nhập tên: ')
    sdt=input('Nhập số điện thoại: ')
    danhba[sdt]=ten
    danhba=dict.update(danhba)
    return danhba
def cap_nhap(danhba):
    while True:
        print('Bạn muốn cập nhập thông tin nào? ')
        chon_cap_nhap=int(input('Nhập lựa chọn :1:Cập nhập tên;2:xóa theo tên: '))
        if chon_cap_nhap==1:
            sdt_cap_nhap=input("Nhập số điện thoại người cần cập nhật: ")
            for key,Value in danhba.items():
                if sdt_cap_nhap == key:
                    ten_moi=input('Nhập tên mới :')
                    danhba[key]=ten_moi
        elif chon_cap_nhap==2:
            chon_xoa=input('Xóa theo tên hay sdt ? 1:Xóa theo tên,2:xóa theo sdt: ')
            if chon_xoa== '1':
                xoa_ten=input('Nhập tên cần xóa: ')
                xac_nhan=int(input('Bạn có thức sự muốn xóa không ? 1:xóa,2:Không: '))
                if xac_nhan=='1':
                    del danhba[xoa_ten]
                    print('Đã xóa tên',xoa_ten,'trong danh bạ')
                elif xac_nhan=='0':
                    print('Hủy lệnh xóa trong danh bạ')
            elif chon_xoa=='2':
                xoa_sdt=int(input('Nhập số điện thoại cần xóa?'))
                xac_nhan=int(input('Bạn có thực sự muốn xóa không? 1:Có,2:Không:'))



        else:
            print('Chỉ nhập số theo menu cập nhật! ')
        tt_cap_nhap=input('Bạn có muốn tiếp tục cập nhập không (1:TT):(2:Không TT)' )
        if chon_cap_nhap!='0':
            break
    print('ĐÃ CẬP NHẬT XONG!')
print('CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ') 
while True:
    print('Menu: 1:Xem danh bạ;2:Tìm kiếm;3:Thêm mới;4:Cập nhập danh bạ')
    chon=int(input('Chọn chức năng cần làm việc:'))
    if chon==1:
        in_danhba(danhba)
    elif chon==2:
        tim_kiem(danhba)
    elif chon==3:
        them_moi(danhba)
    elif chon==4:
        cap_nhap(danhba)
    else:
        print('Chỉ nhập số theo menu') 
    tt=input('Bạn có muốn tiếp tục không (1:TT): ')
    if tt!='1':
        break
print("Kiểm tra danh bạ hiện tại ",danhba)
del(danhba)      