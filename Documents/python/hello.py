print("Hello World")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x,y,z="blue", "red", "yellow"
print(x)
print(y)
print(z)
x=y=z="orange"
print(x)
print(y)
print(z)
x=10.50
print(type(x))
y=5j
print("Mike Acosta")
myString="abcdefghijk"
print(myString[::-1])
print(myString[2:7:2])
print(myString[::3])
print(myString[2:7])
print("Hello World"[8])
print(myString[:-1])
print(f"{5//3:.2f}")
day1=100
day2=7
if (day1 - day2) < 100:
    print(f"Its {day1-day2} days left before Christmas ")
    


mood="Sad"
if mood=="Happy":
    print("Yehey! Masaya ako nasa mood ako")
else:
    print("Di masaya kaya malungkot")
    
for x in range(1,11):
    print(f"{x:5}", end="")
    if (x%5==0):
        print("")
        
for x in range(1,5):
    for y in range(6,10):
        print(f"{x}{y} ", end="")
    print("")
    print("1234")
        
        
