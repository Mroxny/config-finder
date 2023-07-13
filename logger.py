from datetime import datetime
import os

class Logger:
    def __init__(self):
        self.file_name = "finder_log.log"
        self.log_dir = 'logs'
        self.verbose_mode = False

    

    def add_to_log(self, msg, verbose = False):
        msg = self.format_message(msg)        

        if not os.path.isdir(self.log_dir):
            self.log_dir = os.path.dirname(os.path.abspath(__file__))
            self.add_to_log("Log directory not found. Switching to project directory")
        
        if self.verbose_mode or verbose:
            print(msg)

        path = os.path.join(self.log_dir, self.file_name)

        self.write_to_file(file_path=path, msg=msg)
        self.remove_oldest_lines(file_path=path, num_lines=10000)


    def write_to_file(self, file_path, msg):
        try:
            with open(file_path, "a") as log_file:
                log_file.write(f'{msg}\n')
        except Exception as e:
            print(self.format_message(e))
        

    @staticmethod
    def remove_oldest_lines(file_path, num_lines):

        with open(file_path, 'r') as file:
            lines = file.readlines()

        if len(lines) >= num_lines:
            new_lines = lines[-num_lines:]

            with open(file_path, 'w') as file:
                file.writelines(new_lines)

            return True
        else:
            return False
    
    @staticmethod
    def format_message(msg):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return f'LOG[{dt_string}]: {msg}'



