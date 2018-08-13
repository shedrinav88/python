
# coding: utf-8

# In[19]:


# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')
def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(cur_folder, dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))
def ping():
    print("pong")
def copy_file():
    from shutil import copyfile
    if not dir_name:
        print("Необходимо вторым параметром указать имя файла, который нужно скопировать")
        return
    try:
        dir_path = os.path.join(cur_folder, dir_name)
        newfile = dir_name + '.copy'   
        copyfile(dir_path, newfile)
        print('создана копия файла {}. Название копии {}'.format(dir_name, newfile))
    except FileNotFoundError:
        print('По заданному значению не найден файл. Проверьте корректность написания имени файла'
              ' или попробуйте указать полный путь к файлу')
def remove_file():
    if not dir_name:
        print("Необходимо вторым параметром указать имя файла, который нужно удалить")
        return
    try:
        confirm = input('Вы уверены, что хотите удалить файл {}, выберите Y/N '.format(dir_name))
        if confirm == 'Y' or confirm == 'y':
            dir_path = os.path.join(cur_folder, dir_name)
            os.remove(dir_path)
            print('удалён файл {}'.format(dir_name))
        elif confirm == 'N' or confirm == 'n':
            print('файл не удален!')
            return
        else:
            print('Введена некорректная комбинация. Нужно выбрать Y/N')
    except FileNotFoundError:
        print('По заданному значению не найден файл. Проверьте корректность написания имени файла'
              ' или попробуйте указать полный путь к файлу')
def change_dir():    
    if not dir_name:
        print("Необходимо вторым параметром указать директорию,в которую перейти")
        return
    try:
        path = os.path.join(os.getcwd(), 'text.txt')
        os.chdir(dir_name)
        with open(path, 'w') as f:
            f.write(os.getcwd())
        print('Перешел в новую директорию:', dir_name)
    except FileNotFoundError:
        print('Такая директория не найдена! Вторым параметром укажите полный путь к директории!')
def path_dir():
    print('полный путь текущей директории:', cur_folder)

path = os.path.join(os.getcwd(),'text.txt')
if os.path.isfile(path):
    with open(path,'r') as f:
        cur_folder = str(f.read())
else:
    cur_folder = os.getcwd()    
do = {
"help": print_help,
"mkdir": make_dir,
"ping": ping,
'cp': copy_file,
'rm': remove_file,
'cd': change_dir,
'ls': path_dir
}
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

