import functions as fn
import copy

data = 'input_07test.txt'

logs = fn.Reader(data).get_lines()
tree = []
path = []
level = 0

#   CLASSES
#   =========
class Directory():

    def __init__(self, name: str, path: list, level: int) -> None:
        self.name = name
        self.path = path
        self.level = level
        self.files = {}
        self.directory_size = 0

    def get_level(self) -> int:
        return self.level

    def get_name(self) -> str:
        return self.name

    def get_path(self) -> str:
        return self.path

    def add_file(self,file:str, size:int) -> None:
        self.files.update({file:size})
        return

    def get_file_names(self) -> list:
        return self.files.keys()

    def get_file_sizes(self) -> list:
        return self.files.values()

    def get_directory_size(self) -> int:
        self.directory_size = 0
        for size in self.files.values():
            self.directory_size += size
        return self.directory_size

    def __str__(self) -> str:
        return f'Directory: {self.name}'    

# Parse the log file
for log in logs:

    # get current path and level in tree hierarchy
    if log[:7] == '$ cd ..':
        action = 'up one level'
        level -= 1
        path.pop()
    elif log[:4] == '$ cd':
        action = 'move to directory: ' + log[5:]
        current = log[5:]
        level += 1
        path.append(log[5:])

    # build directory objects
    elif log[:4] == '$ ls':
        action = 'list files'

    elif log[:3] == 'dir':
        action = 'new directory:' + log[4:]
        path_copy = copy.deepcopy(path)
        path_copy.append(log[4:])
        tree.append(Directory(log[4:],path_copy,level))
        #print(path, log[4:], path_copy)
        
    else:
        file_to_add = log.split(' ')
        for directory in tree:
            #print(file_to_add, path, directory.get_path(), directory)
            if directory.get_path() == path:
               directory.add_file(file_to_add[1],int(file_to_add[0]))

    #print(level, path, log)

# Calculate size including child directories    

for item in tree:
#    print(f'{item}, level: {item.get_level()}, {item.get_path()}, {item.get_file_names()}, {item.get_file_sizes()}, {item.get_directory_size()}')
    print(f'{item}, level: {item.get_level()}, {item.get_path()}, {item.get_directory_size()}')

    for child in tree:
        #if len(child.get_path()) > 2:

            print(f'{child}, level: {child.get_level()}, {child.get_path()}, {child.get_directory_size()}', {item.get_path() == child.get_path()})


# still stuck needing to figure out recursion !!!
# directories and sizes seem okay
