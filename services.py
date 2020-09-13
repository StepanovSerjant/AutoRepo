import os


def project_arg_info():
    """ Функция информирования об некорретно введенном аргументе типа проекта """
    
    print('-w - указывает на создание web проекта')
    print('-p - указывает на создание python проекта')


def project_name_info():
    """ Функция информирования об отсутствии имени проекта"""

    print('Вы не указали имя проекта!\n')
    print('Корректная команда запуска скрипта выглядит следующим образом:')
    print('python main.py {-w, -p} <имя вашего проекта (можно без кавычек)>')       


def create_dir(name, path=None, returning=False):
    """ Функция создания директории """
    if path != None:
        name = os.path.join(path, name)    
    os.mkdir(name)  
    if returning == True:
        return os.path.abspath(name)

def create_file(name, path=None, text=None):
    """ Функция создания файла """
    if path != None:
        name = os.path.join(path, name)
    with open(name, 'tw', encoding='utf-8') as f:
        if text != None:
             f.write(text)
             