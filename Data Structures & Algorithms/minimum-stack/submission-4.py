class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min)==0:
            self.min.append(val)
        else:
            self.min.append(min(val,self.min[-1]))


    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print("min ", self.min)
        return self.min[-1]
