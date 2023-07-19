import logging

class Logger():
    def __init__(self, file_name = "file.log", verbose:bool = False, format = '[%(asctime)s]: %(levelname)s - %(message)s'):
        self.logger = logging.getLogger(__name__)
        self.logfile = file_name
        self.verbose = verbose

        self.handler_cmdline = logging.StreamHandler()
        self.handler_file = logging.FileHandler(self.logfile)

        if self.verbose:
            self.handler_cmdline.setLevel(logging.DEBUG)
        else: 
            self.handler_cmdline.setLevel(logging.ERROR)

        self.handler_file.setLevel(logging.DEBUG)

        log_format = logging.Formatter(fmt=format, datefmt='%Y-%m-%d %H:%M:%S')
        self.handler_cmdline.setFormatter(log_format)
        self.handler_file.setFormatter(log_format)

        self.logger.addHandler(self.handler_cmdline)
        self.logger.addHandler(self.handler_file)
        self.logger.setLevel(logging.DEBUG)

