#Make a generator to perform the same functionality of the iterator
def generator(input):
    value=1
    for num in range(1,input):
        value=value*num
        yield value
        
for value in generator(5):  
    print(value) 

#Try overwriting some default dunder methods and manipulate their default behavior
class SampleOverride:
    def __init__(self):
        self.name='Test'
    def __str__(self):
        return 'name='+self.name

obj=SampleOverride()
print(obj)

