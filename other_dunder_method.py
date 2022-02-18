class Number:
    def __init__(self, num):
        self.num = num


    def __add__(self, num2):
        print("Lets add qwertyuiop")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply asdfghjkl")
        return self.num * num2.num

    def __str__(self):
        return f'The decimal number is {self.num}.'

    def __len__(self):
        return 2

n = Number(1238)
print(n)
print(len(n))