#Given a list of names, try printing unique names that are less than 5 character length and doesn't contain the character 'e'. 
#names = ["john", "jake", "jack", "george", "jenny", "jason"]

names = ["john", "jake", "jack", "george", "jenny", "jason"]
unique_names = set(names)
for var in unique_names:
  if len(var)<5 and "e" not in var:
    print(var)

#Given a string python, try printing cython using slicing [start:stop] and concatenation. +
string = "python"
print("c"+string[1:])

#Given a dictionary {"name": "python", "ext": "py", "creator": "guido"}, print both keys and values.
dictSample= {"name": "python", "ext": "py", "creator": "guido"}
print(dictSample)
for key,value in dictSample.items():
  print(f"Key:{key},Value:{value}")

  #Do FizzBuzz in Python
  list = range(1,101)
  for item in list:
    if item%3==0:
      print("Fizz")
    elif item%5==0:
      print("Buzz")
    elif item%15==0:
      print("FizzBuzz")
    else:
      print(item)


#Guessing Game. Accept a guess number and tell us if it's higher or less than the hardcoded number
x=int(input("Please enter number of your choice:"))
y=20
if x<y:
  print("input value is less than expected")
elif x>y:
  print("input value is greater than expected")
else:
  print("Value is as expected")
