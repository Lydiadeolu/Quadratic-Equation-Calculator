print("hello adeolu")
print("Enter a,b,c for a quadratic in the form of ax*2 + bx + c =0 to find the root of the quadratic.")

a = input("what is the value of a? ")
b = input("what is the value of b? ")
c = input("what is the value of c? ")

a = float(a)
b = float(b)
c = float(c)

determinant = b ** 2 - 4 * a * c
#print(determinant)
min_x = (-b - (determinant) ** (1 / 2)) /(2 * a)
max_x = (-b + (determinant) ** (1 / 2)) /(2 * a)

print(f"The lesser x is equal to {min_x} and the greater x is qual to {max_x}")

