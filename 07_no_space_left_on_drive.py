import functions as fn

data = 'input_07test.txt'
#data = 'input_07.txt'

logs = fn.Reader(data).get_lines()
        
class File():

    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
pp
    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return int(self.size)    

    def __str__(self) -> str:
        return f'File name: {self.name}, File size: {self.size}'

class Directory():

    def __init__(self, name :str, parent :str) -> None:
        self.name = name
        self.parent = parent
        self.contents = {}

    def add_content(self, name :str, content :object) -> None:
        self.contents[name] = content
        return    

    def get_name(self) -> str:
        return self.name

    def get_parent(self) -> str:
        return self.parent

    def  get_contents(self) -> list:
        return [ x for x in self.contents.keys()]
        
    def get_size(self) -> int:
        return sum( [x.get_size() for x in self.contents.values()] )
    
    def __str__(self) -> str:
        return f'Directory: {self.name}'    


# setup start of directory tree
directories = {}
directories['/'] = Directory('/', '')

current_directory = '/'


directories['/a'] = Directory('a','/')
directories['/d'] = Directory('d','/')
directories['/a/e'] = Directory('e','/a')

for log in logs:
    if log[:7] == '$ cd ..':
        action = 'up one level'
        #path = directories[path].get_parent()
        #print(action, directories[path].get_parent())
        #level -= 1
    elif log[:4] == '$ cd':
        target = log[5:]
        action = 'move to directory: ' + target
        print(action, directories[current_directory].get_parent()+'/'+target)
        current_directory = directories[current_directory].get_parent()+'/'+target

        #current = log[5:]
        #level += 1
    elif log[:4] == '$ ls':
        action = 'list files'
    elif log[:3] == 'dir':
        action = 'new directory: ' + log[4:]
        #name = log[4:]
        #directories[path + '/' + name] = Directory(name, path)
    else:
        file_name = log.split(' ')[1]
        file_size = log.split(' ')[0]
        #print(file_name, file_size)
        #directories[path].add_content( file_name, File(file_name, file_size))

    #print(action)


for key, value in directories.items():
    print(key, value, type(value), value.get_name())

#print(directories['/a'].get_contents())
#print(directories['/a'].get_size())
