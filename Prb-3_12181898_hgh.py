def parsing(eqn):
    poly_dict = {}
    A = eqn.split("x^")
    A = "".join(A).split(" ")
    poly_dict[A[1]] = A[0]
    poly_dict[A[4]] = A[2] + A[3] 
    poly_dict[A[6]] = 1.0
    poly_dict[A[8]] = A[7]
    
    pw2coeff = poly_dict
    return pw2coeff


poly_str = input("polynomial string = ")
result = parsing(poly_str)
print(result)


"""
while bool(A.index("-"))
    A[A.index("-")] + A[A.index("-")+1]
    A[A.index("+")] + A[A.index("+")+1]
"""