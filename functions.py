import re

class Reader():
    '''Read lines from a text file into a list.'''

    def __init__(self, file) -> None:
        self.file = file
        with open(file) as f:
            self.lines = f.readlines()

    def get_lines(self) -> list:
       return [x[:-1] for x in self.lines]

    def get_raw_lines(self) -> list:
        '''Unprocessed list including line feeds.'''
        return self.lines

    def __str__(self) -> str:
        return f'List of lines from {self.file}.'

#   For Testing
if __name__  == '__main__':

    input_file = "input_01.txt"
    print( Reader(input_file).get_lines() )