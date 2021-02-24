# Write an iterator yourself 
# Create a class that implements __iter__ and __next__ methods.
# It should accept a string and provide an iterator that traverses every other character in the string i.e. given hello, provide h, l, o and StopIteration on consecutive next calls. 

import sys 
class iterClass:
    def __init__(self, inputVal):
        self.inputVal=inputVal
        self.init=-2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.init<len(self.inputVal):
            self.init +=2
            return self.inputVal[self.init]
        else:
            raise StopIteration

sample = iterClass("Welcome")
nextVal = iter(sample)
print(nextVal.__next__())
print(nextVal.__next__())
print(nextVal.__next__())
print(nextVal.__next__())

#create a CSV file containing names and experience of the participants. Note: Not xls, just a comma separated plain text file.

empDetails = {"Name":"Experience(yrs)","UserA":"8","UserB":"7","UserC":"5"}
try:
    finalFile = open("Data.csv","w") 
    for key,value in empDetails.items():
        finalFile.write(f"{key},{value},")

except:
    print("Some error occured!")


#write a program to traverse the current directory (recursively) and print only python file names.

import os

for root, directories, files in os.walk("."):
    for file in files:
        if str(file[-3:])==".py":
            print(files)



#use standard lib sys to list all the command line args given to your program

import sys
print(sys.argv)


#Rewrite the guessing game program to throw a custom error when the user is out of tries.
#accept input from a user and handle type, value errors
import random

counter = 0
expectedValue = random.randint(1, 10)
for attempt in range(5):
    try:
        inputValue = int(input("Enter value:"))
        if inputValue < expectedValue:
            print("Sorry! Value less than expected value")
        elif inputValue > expectedValue:
            print("Sorry! Value greater than expcted value")
        else:
             print("Good job! your guess is right")
             break
        counter += 1
    except ValueError:
        print("Please enter a integer value")
        
        
#demonstrate key and index errors in an example

try:
    sampleDict = {'sample':'test'}
    print(sampleDict['value'])

except KeyError:
    print("Key Error!")



try:
    sampleList = [1,2,3]
    print(sampleList[3])

except IndexError:
    print("Index Error!")
