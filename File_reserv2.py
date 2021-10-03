import os 
import time 
os.chdir(r'C:\Program Files (x86)\GnuWin32\bin')

source = ['"C:\\Users\\User\\Documents\\Witcher 2\\gamesaves"'] #указали файлы и каталоги для резервного копирования в списке

target_dir = ('C:\\Users\\User\\Documents\\Programms\\butt')#это каталог, в котором мы сохраняем все резервные копии
today = target_dir + os.sep + time.strftime('%Y%M%d') #Именем zip-архива, который мы создаём, будет текущая дата и время, которые генерируются при помощи функции time.strftime(). У него будет расширение .zip, и храниться он будет в каталоге target_dir 
now = time.strftime('%H%M%S') 
# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
   target = today + os.sep + now + '_' + \
comment.replace(' ', '_') + '.zip '
#создаём католог если его нет 
if not os.path.exists(today) : 
    os.mkdir (today)
    print ('католог успешно создан') 
target = today + os.sep + now + '.zip' 
zip_command = "zip -qr {0} {1}".format(target,''.join(source)) #Мы превращаем список source в строку,
#используя уже знакомый нам метод join.

if os.system(zip_command) == 0 : #выполняем команду при помощи функции os.system, которая запускает команду так, как будто она была запущена из системы, т.е. из
#командной оболочки. 
     print('Резервирование удалось')
else : 
    print('Резервирование не удалось')