import functions as fn

data = 'input.txt'
#data = 'input_09.txt'

steps = fn.Reader(data).get_lines()

#print(steps)

# setup variables
xhead = 0
yhead = 0
xtail = 0
ytail = 0

tail_track = []
head_track = []

class Tail():

    def __init__(self) -> None:
        self.xtail = 0
        self.ytail = 0
        self.trail = []

    def move_tail(self, coordinates:tuple) -> tuple:
        xhead = coordinates[0]
        yhead = coordinates[1]

        if abs(yhead - self.ytail) == 2:
            self.xtail += int(xhead - self.xtail)
            self.ytail += int((yhead - self.ytail)/2)
        elif abs(xhead - self.xtail) == 2:
            self.xtail += int((xhead - self.xtail)/2)
            self.ytail += int(yhead - self.ytail)

        self.trail.append( (self.xtail,self.ytail) )

        return ( self.xtail , self.ytail )

    def __str__(self) -> str:
        return f'Unique locations visited: {len(set(self.trail))}'

# parse step and build instructions for head
def build_head_instructions(step:str) -> list:
    '''List of'''
    direction = step[0]
    movements = int(step[1:])

    moves = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}

    return [moves[direction] for x in range(movements)]

def move_head(move:tuple) -> None:
    global xhead
    global yhead

    xhead += move[0]
    yhead += move[1]
    return

def is_move_required() -> bool:
    return abs(xhead - xtail) > 1 or abs(yhead - ytail) > 1

def move_tail() -> None:
    global xtail
    global ytail

    # linear move
    if abs(yhead - ytail) == 2:
        xtail += int(xhead - xtail)
        ytail += int((yhead - ytail)/2)
    elif abs(xhead - xtail) == 2:
        xtail += int((xhead - xtail)/2)
        ytail += int(yhead - ytail)
    return

def track_tail() -> None:
    tail_track.append( (xtail,ytail) )

def track_head() -> None:
    head_track.append( (xhead,yhead) )

for step in steps:
    #print(f'{step}, {build_head_instructions(step)}')

    moves = build_head_instructions(step)
    
    # move the head
    for move in moves:
        move_head(move)

    #print(step, xhead, yhead)  # test move coordinates

        # check for proximity
    
        #print(step, xhead, yhead, is_move_required(), xtail, ytail)  # test move coordinates

        # move the tail
        if is_move_required():
            move_tail()
    
#        print(step, xhead, yhead, is_move_required(), xtail, ytail)  # test move coordinates

        # update coordinates visited
        track_tail()


coordinates_visited = set(tail_track)
#print(tail_track)
#print(coordinates_visited)
print(f'The tail visited {len(coordinates_visited)} positions.')

# remove duplicate coordinates
# count coordinates visited

# ====================================================
xhead = 0
yhead = 0

tail = Tail()

for step in steps:
    moves = build_head_instructions(step)

    for move in moves:
        move_head(move)
#    print(step, xhead, yhead)  # test move coordinates

        tail.move_tail((xhead,yhead))
#        print((xhead,yhead),tail.move_tail((xhead,yhead)))

print(tail)