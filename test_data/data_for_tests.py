import os


class DataForTests:
    def __init__(self):
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')

