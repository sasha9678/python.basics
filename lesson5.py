# if statement
# store data list, tuple, dictionary, set
# loops
# 64 '64'
entered_value = input("Enter a number: ") # str
# print(type(entered_value))
# print(type(71))
# print (type(55.22))
if not entered_value.isdigit():
    print("Please enter a number")
    exit(0) # stop

    score = int(entered_value)  #convert  to a number -- interger

score = 65

if score >= 78:
     print("A")
elif score >= 71 and score <= 77:
     print("A")
elif score >= 64 and score <= 70:
     print("A-")
elif score >= 57 and score <= 63:
     print("B")
elif score >= 51 and score <= 58:
     print("B-")
elif score >= 49 and score <= 53:
    print("C+")
elif score >= 40 and score <= 48:
    print("C")






