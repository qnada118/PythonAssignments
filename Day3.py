#dictionaries
#given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
#make a list of values alone from the above dictionary [1, 4, 9] using list comprehension


nums = [1, 2, 3]
dictSquareValue = {num:num**2 for num in nums}
print(dictSquareValue)
listSquareValues=[num**2 for num in nums]
print(listSquareValues)

#set comprehension
#given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}

inputList = [1, 2, 5, 2, 3, 1, 4, 5]
print(set(inputList))
resultSet = {item**2 for item in set(inputList)}

print(resultSet)

#Given a list of tuples with current and min balances: [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:

#dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}

inputList = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

dictOutput = {name:total for (name,total,min) in inputList if total>=min}

print(dictOutput)

#set of all balances {2000, -52, 900}

inputList = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

setOutput = {total for (name,total,min) in inputList }

print(setOutput)

#list of account holders ["Guido", "Raymond", "Jack", "Brandon"]

inputList = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

setOutput = {name for (name,total,min) in inputList }

print(setOutput)



#dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}

inputList = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

setOutput = {name:min-total for (name,total,min) in inputList if total<min }

print(setOutput)

#list of tuples with name and current balance if the balance is above 0 [("Guide", 2000), ("Jack", 900), ("Brandon", 2000)]

inputList = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

setOutput = {name:total for (name,total,min) in inputList if total>0 }

print(setOutput)

#Write a Developer class that has a code function and a languages list.
#code function should accept a language param and if the language is in the languages list it should print code in <language>.
#resume function that prints languages of the developer.
#Write a SrDeveloper class that inherits Developer and adds review function. review should also be limited to languages list.
#Write a TechLead class that inherits from SrDeveloper and adds design function

class Developer:
  def __init__(self):
    self.languages=["C","Java","Python"]

  def code(self,language):
    if language not in self.languages:
      print("language code not found")
    else:
      print(f"code in{language}")

  def resume(self):
    print(self.languages)

class SeniorDeveloper(Developer)
def _init_(self):
  Developer._init_(self)

def review(self,languageReview):
  self.languages.append(languageReview)
  print(self.languages)

class TechLead(SeniorDeveloper):
  def _init_(self):
    SeniorDeveloper._init_(self)

  def design(self,languageDesign):
    self.languages.append(languageDesign)
    print( self.languages)

