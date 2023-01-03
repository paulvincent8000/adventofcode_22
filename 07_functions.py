# IMPORTS
#--------------------------------------------------------------------

# Classes
#--------------------------------------------------------------------

class Directory():

    def __init__(self, name: str) -> None:
        self.name = name
        self.sub_directories = {}
        self.files = {}

    def mkdir(self, name) -> None:
        '''Make sub-directory'''
        self.sub_directories[name] = Directory(name)
        return

    def ls(self) -> list:
        '''List directory contents'''
        ls = [key for key in self.sub_directories.keys()] + [key for key in self.files.keys()]
        return ls

    def add_file(self, name: str, size: int) -> None:
        '''Add a file'''
        self.files[name] = size
        return

    def get_size(self) -> int:
        '''Total size of this directory'''
        pass

    def cd(self, name: str) -> object:
        '''Move to new directory and provide directory object'''
        return self.sub_directories[name]

    def __str__(self) -> str:
        return f"Directory: {self.name}."

if __name__ == '__main__':

    parent = Directory('parent')

    parent.mkdir('child1')

    parent.add_file('test_file', 120)

    print( parent.ls() )

    child = parent.cd('child1')

    print(child)

    #print(parent.sub_directories)

    #print(parent)