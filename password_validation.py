def check_pass(pwd):
    if len(pwd) < 8:
        print('Mat khau cua ban co it hon 8 ky tu')
    elif not any(i for i in pwd if i.isnumeric()):
        print('Mat khau cua ban khong chua chu so')
    elif not any(i for i in pwd if i.isupper()):
        print('Mat khau cua ban khong chua ky tu viet hoa')
    elif not any(i for i in pwd if not i.isalnum()):
        print('Mat khau cua ban khong chua ky tu dac biet')
    elif any(i for i in range(len(pwd)-2) if pwd[i:i+3].isnumeric()):
        print('Mat khau cua ban chua 3 chu so lien tiep')
    else:
        print(f'Mat khau {pwd} hop le')
        return False

while True:
     pwd = input('Nhap mat khau: ')
     if check_pass(pwd) == False:
         break
