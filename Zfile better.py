import zipfile 
import os 
reserv = ('C:\\Users\\User\\Documents\\Programms\\Reserv')
path = (r'D:\Games\steamapps\common\GarrysMod\garrysmod\resource') 
name = input('Название файла:')
file_dir = os.listdir(path)
os.chdir(''.join(reserv)) 
with zipfile.ZipFile(''.join(name)+'.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:  
        add_file = os.path.join(path , file,) 
        zf.write(add_file) 
    print('Все нормально')
    
