class Int2String():
    @abstractmethod
    def convert(self,i):
        pass
class Displayer():
    @abstractmethod
    def display(self,s):
        pass


class ProblemSolver:
    def __init__(self, converter:Int2String, displayer: Displayer):
        self.converter = converter
        self.displayer = displayer
        
    def solve(self):
        for i in range(1,100):
            self.display(self.convert(i))