class MyComplex:
    def __init__(self, value):
        if value.find("i") != -1:
            if value.find("+") != -1:
                self.real = int(value[:value.find("+")])
                self.imag = int(value[value.find("+"):-1])
            elif value.find("-") != -1:
                self.real = int(value[:value.find("-")])
                self.imag = int(value[value.find("-"):-1])
        else:
            self.real = int(value)
            self.imag = 0
            
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return MyComplex("{}{}i".format(real,imag))
        
    def __str__(self):
        return "{}{}i".format(self.real,self.imag)

a = MyComplex("1+2i")
b = MyComplex("3-4i")
print(a+b)