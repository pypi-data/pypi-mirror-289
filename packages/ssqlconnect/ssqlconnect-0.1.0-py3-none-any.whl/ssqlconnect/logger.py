import logging

class Log():
    def __init__(self, name : str = "__defaultLogger__"):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("mysql.connector").setLevel(logging.WARNING)
        self.logger = logging.getLogger(name)