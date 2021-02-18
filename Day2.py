
#Improvise the guessing game from yesterday by providing 3 tries to the player
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

#Given a list ['a', 'b', ...] print elements along with their position like 0: a, 1: b one per line
import string
values = list(string.ascii_lowercase)
for key,value in enumerate(values):
  print(f"{key}:{value}")

#Loop over a dict and print the value and key in the format value belongs to key
dictSample = {"name":"Nada", "sex":"female", "age":"30"}
for key,value in dictSample.items():
  print(f"{value} belongs to {key}")

#Demonstrate the else clause being invoked in a while loop. try the opposite as well.
i=3;
while(i<3):
  if(i%2==0):
    print("Number is even")
    break;
else:
  print("No numbers even")

#write an add function that accepts two numbers and returns their sum 
#use type hints
#use docstring

def addNumbers(num1,num2):
      '''Accepts input for two numbers and returns their sum'''
      sum=num1+num2
      return sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(addNumbers.__doc__)
print(addNumbers(num1, num2))


#write a function that accepts any number of kwargs and prints the number of orgs
def displayArgs(*args):  
    for arg in args:  
      print (arg) 

    

displayArgs("America", "France", "India", "Africa") 

#Do list comprehension to get odd numbers' squares from this list: [1, 3, 3, 4, 5, 6]
inputList = [1, 3, 3, 4, 5, 6]

outputList = [num** 2 for num in inputList if num%2 != 0]

print(outputList)


#write a lambda expression to return average given a total and count

totalValue = int(input("Enter the Total Value : "))

countValue = int(input("Enter the Count Value : "))

avg = lambda totalValue, countValue : totalValue /countValue

print(f"Average of {totalValue} having count {countValue} = {avg(totalValue,countValue)}")
