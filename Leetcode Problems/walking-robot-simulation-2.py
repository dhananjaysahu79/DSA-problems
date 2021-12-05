class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.rPos = [0,0]
        self.cards = ['East','North','West','South']
        self.dir = 0

    def step(self, num: int) -> None:
        width = self.width
        height = self.height
        num = num % (2 * (height+width+2) - 4)
        if not num and not sum(self.rPos): self.dir = 3
        while num > 0:
            if self.dir == 0:
                if self.rPos[0] + num > width:
                    num = self.rPos[0] + num - width
                    self.rPos[0] = width
                    self.dir = 1
                else:
                    self.rPos[0] = self.rPos[0] + num
                    num = 0
            elif self.dir == 1:
                if self.rPos[1] + num > height:
                    num = self.rPos[1] + num - height
                    self.rPos[1] = height
                    self.dir = 2
                else:
                    self.rPos[1] = self.rPos[1] + num
                    num = 0
            elif self.dir == 2:
                if self.rPos[0] - num < 0:
                    num -= self.rPos[0]
                    self.rPos[0] = 0
                    self.dir = 3
                else:
                    self.rPos[0] -= num
                    num = 0
            else:
                if self.rPos[1] - num < 0:
                    num -= self.rPos[1]
                    self.rPos[1] = 0
                    self.dir = 0
                else:
                    self.rPos[1] -= num
                    num = 0
            

    def getPos(self) -> List[int]:
        return self.rPos
        

    def getDir(self) -> str:
        return self.cards[self.dir]