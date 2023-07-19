import os

class ConfigFinder:
    def __init__(self, log_class):
        self.config_paths = []
        self.exclude = []
        self.include = []
        self.log = log_class.logger

    def add_config_path(self, path):
        if path not in self.config_paths:
            self.config_paths.append(path)
    
    def add_files_to_exclude(self, file_type:list):
        for f in file_type:
            if f not in self.exclude:
                self.exclude.append(file_type)
        self.log.debug(f"Added files to exclude: {self.exclude}")

    def add_files_to_include(self, file_type:list):
        for f in file_type:
            if f not in self.include:
                self.include.append(file_type)
        self.log.debug(f"Added files to exclude: {self.include}")


    def find_unique_config_files(self):
        config_files = {}

        for path in self.config_paths:
            self.log.debug(f'Searching for files in "{os.path.abspath(path)}"')

            for f in os.listdir(path):
                f = self.check_config_file(f)
                if f is not None:
                    config_files[f] = os.path.join(path, f)

            self.log.debug(f'All found files: {config_files}')
            
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
        

        self.log.debug(f'Found new file: {file}')
        return file
