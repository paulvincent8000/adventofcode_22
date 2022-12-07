import functions as fn

data = 'input.txt'

logs = fn.Reader(data).get_lines()

# find directory structure
for log in logs:
    if log[:7] == '$ cd ..':
        action = 'up one level'
    elif log[:4] == '$ cd':
        action = 'move to directory: ' + log[5:]
    elif log[:4] == '$ ls':
        action = 'list files'
    elif log[:3] == 'dir':
        action = 'new directory:' + log[4:]
    else:
        action = log.split(' ')
    print(action)