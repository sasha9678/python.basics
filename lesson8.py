# Dictionary
# list[], tuple(), dictionary{}
from lesson7 import people

student = { "name ": "Sara Ajako", "id": 456, "age": 22, "gender": "F"}

print(student[ "name "])  #key
print(student)

student["weight"] = 61

print(student)

# set
people = {"Jane", "Bill", "Kevo", "Said", "Jane" }
print(people)
people.add("Willy")
print(people)
print(len(people))    #count
people.discard("Kevo")
print(people)
