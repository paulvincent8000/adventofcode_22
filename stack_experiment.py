class Person():

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.children = []

    def create_child(self, name: str, age: int) -> object:
        self.children.append(Person(name, age))
        return
    
    def get_last_child(self) -> object:
        return self.children[-1]

    def update_age(self, age:int) -> None:
        self.age = age
        return

    def __str__(self) -> str:
        return f"I'm {self.name}, aged {self.age} with {len(self.children)} children"


if __name__ == '__main__':

    pass