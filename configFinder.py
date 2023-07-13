import os
import logger

class ConfigFinder:
    def __init__(self):
        self.config_paths = []
        self.exclude = []
        self.include = []
        self.log = logger.Logger()


    def add_config_path(self, path):
        if path not in self.config_paths:
            self.config_paths.append(path)
    
    def add_files_to_exclude(self, file_type):
        if file_type not in self.exclude:
            self.exclude.append(file_type)
            self.log.add_to_log(f"Added files to exclude: {file_type}")


    def add_files_to_include(self, file_type):
        if file_type not in self.include:
            self.include.append(file_type)
            self.log.add_to_log(f"Added files to include: {file_type}")


    def find_unique_config_files(self):
        config_files = {}


        for path in self.config_paths:
            self.log.add_to_log(f'Searching for files in "{os.path.abspath(path)}"')

            for file in os.listdir(path):
                file = self.check_config_file(file)
                if file is not None:
                    config_files[file] = os.path.join(path, file)

            self.log.add_to_log(f'All found files: {config_files}')
            

        return config_files

    def check_config_file(self ,file):

        # If there are files to include
        if len(self.include) > 0:
            file_type = str(file).rsplit(".",1)
            if len(file_type) > 1 and file_type[1] not in self.include:
                return None 

        # If there are files to exclude
        if len(self.exclude) > 0:
            file_type = str(file).rsplit(".",1)
            if len(file_type) > 1 and file_type[1] in self.exclude:
                return None 
        

        self.log.add_to_log(f'Found new file: {file}')
        return file




