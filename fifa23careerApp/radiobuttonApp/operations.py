class Operations:

    def calculate_sum(self, a, b):
        return a +b

    def calculate_difference(self, a, b):
        return a-b

    def calculate_multiplication(self, a, b):
        return a*b

    def calculate_division(self, a, b):
        if int(b) == 0:
            return "ERROR"
        else:
            value = "{:.2f}".format(a/b)
            return value

    def calculate_power(self, a, b):
        return pow(a,b)

    def check_numbers(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return True
        else:
            return False
