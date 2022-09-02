#Primitive Data Types

#String
print("Andrei", type("Andrei"))

#Integer
print(123456, type(123456))

#Float
print(25.23, type(25.23))

#Boolean
print(5==5, type(5==5))

print("-------------------------")

# Variable Declaration
name = "John"
print(name, type(name))

print("-------------------------")
age=24
height = 1.91
weight = 95
bmi = weight/(height**2)

print("Your height is", height, "m")

print("Your weight is", weight, "kg")

print("Your BMI is", bmi)

# String Formatting
print(f'{name} is {age} years old and your BMI is {bmi:.2f}')
print('{} is {} years old and your BMI is {:.3f}'.format(name,age,bmi))
print('{n} is {a} years old and your BMI is {b:.4f}'.format(n=name,a=age,b=bmi))