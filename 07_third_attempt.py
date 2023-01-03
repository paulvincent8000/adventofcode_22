# IMPORTS
#--------------------------------------------------------------------

# Classes
#--------------------------------------------------------------------

class Directory():

    def __init__(self, name: str) -> None:
        self.name = name
        self.sub_directories = {}
        self.files = []

    def mkdir(self, name) -> None:
        '''Make sub-directory'''
        pass

    def ls(self) -> list:
        '''List directory contents'''
        pass

    def add_file(self, file: object) -> None:
        '''Add a file'''
        pass

    def get_size(self) -> int:
        '''Total size of this directory'''
        pass

    def cd(self, name: str) -> object:
        '''Move to new directory and provide directory object'''
        pass

    def __str__(self) -> str:
        return f"Directory {self.name}."
