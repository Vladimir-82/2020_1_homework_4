class ass:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def get_info(self):
        return self.x, self.y
    def __add__(self, x, y):
        res = x + y
        return res

one=ass(2,3)
print(one.get_info())

print(one.__add__(4,5))