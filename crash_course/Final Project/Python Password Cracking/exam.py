from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

for i in range(ord('a'), ord('z') + 1):
    find_me = chr(i)
    for j in range(ord('a'), ord('z') + 1):
        find_me += chr(j)
        secret_password = find_me + 'bcmpda'
        if unzip_with_7z(zip_file_path, dest_path, secret_password) == True:
            print(secret_password)
            break
        find_me = chr(i)



