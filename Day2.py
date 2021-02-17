import random
guessCount = random.randint(1,11)

for count in range(3):
    x=int(input("Please enter number of your choice:"))
    if x<guessCount:
      print("input value is less than expected")
    elif x>guessCount:
      print("input value is greater than expected")
    else:
      print("input value as expected")
      break


import string
values = list(string.ascii_lowercase)
for key,value in enumerate(values):
  print(f"{key}:{value}")
