def clousre_fun(coeff):
    def a(x):
        def b(y):
            return coeff * x ** y
        return b
    return a

        
    
    
coeff = float(input("coeff = "))
n_power = int(input("power = "))
x = float(input("x = "))

y = clousre_fun(coeff)(n_power)(x)

output_format = "%.1f*%.1f^%d = %.1f"
print( output_format % (coeff,x,n_power,y))

