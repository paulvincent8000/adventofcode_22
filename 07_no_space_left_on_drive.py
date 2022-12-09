import functions as fn

data = 'input_07test.txt'
#data = 'input_07.txt'

logs = fn.Reader(data).get_lines()
        
class File():

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return int(self.size)    

    def __str__(self) -> str:
        return f'File name: {self.name}, File size: {self.size}'

class Directory():

    def __init__(self, name, parent, level) -> None:
        self.name = name
        self.parent = parent
        self.level = level
        self.children = []
        self.files = []

    def add_file(self, file :object) -> None:
        self.files.append(file)
        return    

    def get_files(self) -> list:
        return self.files

    def get_level(self) -> int:
        return self.level

    def get_name(self) -> str:
        return self.name

    def get_parent(self) -> str:
        return self.parent

    def get_total_size(self) -> int:
        self.total_size = 0
        for file in self.files:
            self.total_size += file.get_size()
        return self.total_size

    def add_children(self, child : object) -> None:
        self.children.append(child)
        return

    def get_children(self) -> list:
        if len(self.children) > 0:
            return self.children
        else:
            return ['']

    def __str__(self) -> str:
        return f'Directory: {self.name}'    


# find directory structure
level = 0
tree = [Directory('/', '', level)]
current = '/'

for log in logs:
    if log[:7] == '$ cd ..':
        action = 'up one level'
        level -= 1
    elif log[:4] == '$ cd':
        action = 'move to directory: ' + log[5:]
        current = log[5:]
        level += 1
    elif log[:4] == '$ ls':
        action = 'list files'

    elif log[:3] == 'dir':
        action = 'new directory:' + log[4:]
        new_directory = Directory(log[4:], current, level)
        tree.append(new_directory)
        for directory in tree:
            if directory.get_name() == current:
                directory.add_children(new_directory)
    else:
        action = log.split(' ')
        new_file = File(action[1], action[0])
        for directory in tree:
            if directory.get_name() == current:
                directory.add_file(new_file)
    #print(action)

#print('-------')

#for directory in tree:
    #print(directory, directory.get_total_size(), directory.get_children())
    

#    for subdirectory in directory.get_children():
#        print(directory, subdirectory, directory.get_total_size())
  
#print(tree[2], tree[2].get_children()[0])

# Recursive
path = ['/']
paths = [['/']]

# build the sizes
for path in paths:
    size_cumm = 0
    for step in reversed(path):
        for directory in tree:
            if directory.get_name() == step and directory.get_total_size() < 1000000:
                size = directory.get_total_size()
                size_cumm += size
                #print(path, step, directory.get_name(), size, size_cumm, mega_size)

# find levels in hierarchy
levels = max([directory.get_level() for directory in tree])

# build the hierarchy using levels start with children
directory_list = []
for level in reversed(range(1, levels + 1)):
    for directory in tree:
        if directory.get_level() == level:
            directory_list.append(directory)
            #print(level, directory.get_name(), directory.get_parent(), directory.get_total_size())

        for subdirectory in tree:
            if subdirectory.get_level() == level+1 and subdirectory.get_parent() == directory.get_name():
                directory_list.append(subdirectory)

overal_size = 0
for item in directory_list:
    size = item.get_total_size()
    if size > 100000:
        size = 0
    overal_size += size
    #print(item, size, overal_size)

print(overal_size)
