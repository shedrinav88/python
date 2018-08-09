
# coding: utf-8

# In[ ]:


import os

def make_dir():
    try:
        dir_name = input('Напишите название создаваемой директории: ')
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.mkdir(dir_path)
        print('Создал новую директорию:', dir_path)
    except FileExistsError:
        print('Ай-ай-ай! Нужно другое имя! Директория с таким именем уже существует!')

def remove_dir():
    try:
        dir_name = input('Напишите название директории, которую необходимо удалить: ')
        dir_path = os.path.join(os.getcwd(), dir_name)
        os.rmdir(dir_path)
        print ('Удалена директория:', dir_path)
    except OSError:
        print('Директорию нельзя удалить, т.к. она не пустая!')

def show_dir():
    return print('Содержимое текущей директории:', os.listdir())
    

def open_folder():
    try:
        dir_name = input('Напишите название папки, в которую нужно перейти: ')
        os.chdir(dir_name)
        print('Перешел в новую директорию:', os.getcwd())
    except FileNotFoundError:
        print('Такая директория не найдена! Попробуйте снова зайти в данный пункт меню и ввести полный путь к директории!')

