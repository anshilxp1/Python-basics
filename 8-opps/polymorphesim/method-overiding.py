class animal:
    def speak(self):
        print("animals make sound")
class dog(animal):
    def speak(self): #methode overriding
        print("dog barks")
class cat (animal):
    def speak(self):  #methode overriding
        print("cat meows")

d=dog()
d.speak() # same methode call but its behavior is diff-diff
c=cat()
c.speak()        
