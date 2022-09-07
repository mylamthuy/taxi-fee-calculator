gia_4_0_8=11000
gia_4_30=15300
gia_4_31=12100

gia_7_0_8=12000
gia_7_30=16100
gia_7_31=13800

loai_xe=int(input('Loai xe (chi nhap 4 hoac 7): \n'))
so_km=int(input('So km: \n'))
thoi_gian_cho=int(input('Thoi gian cho: \n'))

if thoi_gian_cho > 5:
    tien_cho=(thoi_gian_cho-5)*750

if loai_xe == 4:
    if so_km <= 0.8:
        tien_di_chuyen = gia_4_0_8
    elif so_km < 31:
        tien_di_chuyen = gia_4_0_8 + (so_km - 0.8)*gia_4_30
    else:
        tien_di_chuyen = gia_4_0_8 + (30 - 0.8)*gia_4_30 + (so_km - 30)*gia_4_31

if loai_xe == 7:
    if so_km <= 0.8:
        tien_di_chuyen = gia_7_0_8
    elif so_km < 31:
        tien_di_chuyen = gia_7_0_8 + (so_km - 0.8)*gia_7_30
    else:
        tien_di_chuyen = gia_7_0_8 + (30 - 0.8)*gia_7_30 + (so_km - 30)*gia_7_31

tien_cuoc = tien_cho + tien_di_chuyen

print('Tien cho = (%d - 5)*750 = %.1f' %(thoi_gian_cho,tien_cho))
print('Tien di chuyen = ',tien_di_chuyen)
print('Tien cuoc = %.1f + %.1f = %.1f' %(tien_cho,tien_di_chuyen,tien_cuoc))