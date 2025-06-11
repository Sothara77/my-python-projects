import random

def randomstudent():
    list = ["barbara", "ponleu", "philip"]
    print(random.choice(list))
    
randomstudent()

def percentagecalculation(percentage, value):
    return (percentage*value) / 100
    
print(percentagecalculation(20,80))
