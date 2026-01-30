import random
so = random.randint(1,100)
a = int(input('Nhap so du doan: '))
print('So ngau nhien: ',so)

if a > so :
    print('So du doan Lon hon so doan: ',a,'>',so)
elif a < so:         
    print('\nSo du doan Nho hon so doan: ',a,'<',so)
else:
    print('\nChuc mung da doan dung', a,"=",so)
