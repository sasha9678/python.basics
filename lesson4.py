# maths functionality
import math
from multiprocessing.spawn import old_main_modules

x = 98
square_root = math.sqrt(x)
print("Root is ", square_root)

rounded = round(square_root, 2)
print("Rounded to two decimal places", rounded)

# call a function
y = round(8.43265)
print(y)
print(round(4.444444,  1))
print(math.pow(2, 3))

round(8.6667, 2)

name = "sara amoit ajako judith"
print (len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.swapcase())
print(name.capitalize())

post = "This thing is easy and fluent"
new_post = post.replace("fluent",  "flowing")
print(post)
