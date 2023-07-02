import random


class generator:

    def __init__(self):
        Logical = False
        while not Logical:
            self.topNum = int(input("choose the highest number"))
            self.lowNum = int(input("choose the lowest number"))
            if self.topNum > self.lowNum >= 0:
                Logical = True

    def generateAns(self):
        answer = random.randint(self.lowNum, self.topNum)
        return answer
