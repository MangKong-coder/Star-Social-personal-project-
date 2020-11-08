class dog():
   def __init__(self):
       print('I have a dog')
       
   def age(self):
       print('My dog is 10 years old')
          
   def name(self):
       print('My dog\'s name is Jeff')

class mydog(dog):
    def __init__(self):
        dog.__init__(self)
        print('It\'s very cute')
    
dogie = mydog()
print(dogie.age())
