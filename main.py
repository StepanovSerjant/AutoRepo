import os
import sys

import services
import settings
import managers


# https://husl.ru/questions/773479
# https://ru.stackoverflow.com/questions/773479/Запуск-скриптов-python-через-cmd-exe-без-полного-пути-к-скрипту
def main():
    """ Основная функция. Парсит аргументы и запускает соответствующую функцию создания проекта. """

    args = [arg for arg in sys.argv if '.py' not in arg]
    try:
        project_type = args[0]
    except IndexError:
        print('Вы не указали никаких аргументов!')
        return services.project_arg_info()

    if project_type in settings.STRUCTURES:
        project_name = ' '.join(args[1:len(args)])
        project_structure = settings.STRUCTURES[project_type]
        
        manager = managers.ProjectManager(settings.PATH, project_name)
        manager.create_project(project_structure)
    elif '-' not in project_type or project_type not in settings.STRUCTURES:
        print('Вы указали не существующий аргумент типа проекта!')
        return services.project_arg_info()


if __name__ == '__main__':
    main()
