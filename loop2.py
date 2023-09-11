base = float(input("Enter the base: "))
exp  = int(input("Enter the exponent(a non-negative integer): "))

result = 1

if exp < 0:
    print("Exponent must be a non-negative integer")
else:
    for i in range(exp):
        result *= base
        
print(f'{base}^{exp} = {result}')    