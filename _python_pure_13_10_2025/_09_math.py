import math
from random import randint, uniform

print("PI:",math.pi)
print("E:",math.e)


print("Karekök 16",math.sqrt(16))
print("2 ^ 5: ",math.pow(2,5))
print("Floor 4.1: ", math.floor(4.1))
print("Ceil 4.1: ", math.ceil(4.1))
print("Faktöriyel 5: ",math.factorial(5))

number1 =[1,2,3,4,5,6]

## Aggregate Functions

print("Max: ", max(number1))
print("Min: ", min(number1))
print("Sum: ", sum(number1))
print("Average: ", sum(number1)/len(number1))

## Logarithms

print("Log 10", math.log10(100))
print("Log 10", math.log(100))
print("Sin90: ", math.sin(90))
print("Cos90: ", math.cos(90))
print("Radyan 90: ",math.radians(90))
print("Degree PI/2: ", math.degrees(math.pi/2))

# Random functions
print("Rastgele sayılar 1-100: ", randint(1,100))
print("Ondalıklı sayı 0-1: ", uniform(0,1))
