import os
import sys

import services  


class FolderManager:
    """ Строка документации """

    def __init__(self, path):
        self.path = path

    def file_handler(self, file):
        try:
            name, text = file['name'], file['text']
            services.create_file(name, path=self.path, text=text)
        except OSError as e:
            print(e)
            print(f'Файл {name} не был создан, так как файл с таким именем уже существует!')
        except KeyError:
            print(f'Файл {name} не был создан, так как вы не указали необходимые ключи!')

    def folder_handler(self, folder):
        name = folder['name']
        try:
            services.create_dir(name, path=self.path)
            self.path = os.path.join(self.path, name)
        except OSError as e:
            print(e)
            print('Не создал папку')

        if 'files' in folder:
            for file in folder['files']:
                self.file_handler(file)
        
        if 'folders' in folder:
            for folder in folder['folders']:
                self.folder_handler(folder)


class ProjectManager(FolderManager):
    """ Строка документации """

    def __init__(self, path, project_name):
        super().__init__(path)
        self.project_name = project_name

    def create_project(self, structure):
        if not self.project_name:
            return services.project_name_info()
        structure['name'] = self.project_name
        self.folder_handler(structure)
