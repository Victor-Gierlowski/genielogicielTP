class FizzBuzz:
    def convert(self, number):
        out = ""
        if(number % 3 == 0):
            out += "Fizz"
        if(number % 5 == 0):
            out += "Buzz"
        if(out == ""):
            out = str(number)
        return out

