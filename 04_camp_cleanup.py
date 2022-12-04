import functions as fn

class ElfPair():

    def __init__(self, sections:str) -> None:
        self.sections = sections
    
    # split assignments into pairs
    def split_sections(self) -> list:
        self.sections_list = self.sections.split(',')
        return self.sections_list

    # get start and end values of sections   
    def split_start_end(self) -> list:
        self.a = self.sections_list[0].split('-')
        self.b = self.sections_list[1].split('-')

        self.a_start = int(self.a[0])
        self.a_end = int(self.a[1])
        self.b_start = int(self.b[0])
        self.b_end = int(self.b[1])
        
        return [self.a_start, self.a_end, self.b_start, self.b_end]

    def is_fully_contained(self) -> bool:
        a_in_b = self.a_start >= self.b_start and self.a_end <= self.b_end
        b_in_a = self.a_start <= self.b_start and self.a_end >= self.b_end
        return a_in_b or b_in_a


    def __str__(self) -> str:
        return self.sections


# collect the input
#data = 'input.txt'
data = 'input_04.txt'

lines = fn.Reader(data).get_lines()


class Assignments():

    def __init__(self, assignments) -> None:
        self.assignments = assignments
        
    def get_all_assignments(self) -> list:
        return self.assignments

    # search for overlaps

    # keep count of overlaps

    def __str__(self) -> str:
        return f'List of assignments: {self.assignments}'


# setup assignments
all_assignments = Assignments(lines)

score = 0

for assignment in all_assignments.get_all_assignments():
    elf_pair = ElfPair(assignment)
    elf_pair.split_sections()
    elf_pair.split_start_end()
    if elf_pair.is_fully_contained():
        score += 1
    print(assignment, elf_pair.is_fully_contained(), score)

#print(all_assignments)
#sections = '2-4,6-8'
#section1 = sections.split(',')[0]
#section2 = sections.split(',')[1]
#print(sections, section1, section2)




