import math

print("Hello User!")
print("This program helps you to solve:")
print("Quadratic equations")
print("Lets start")

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
D = b**2 - 4 * a * c

def Disc(a,b,c,D):
	print("Discriminant:")
	print(D)

def Main(a,b,c,D):
	x1 = (-b - math.sqrt(b**2-4*a*c))/2*a
	x2 = (-b + math.sqrt(b**2-4*a*c))/2*a
	Disc(a,b,c,D)
	print("x1:")
	print(x1)
	print("x2:")
	print(x2)

Main(a,b,c,D)
