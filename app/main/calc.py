
class Calc():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def divide(self):
        try:
            if self.num1 / self.num2:
                return self.num1 / self.num2
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('ZeroDivisionError')
            return 0

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def reminder(self):
        try:
            if self.num1 % self.num2:
                return self.num1 % self.num2
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print('ZeroDivisionError')
            return 0
