# Animal.py
# by J Alex Long
# created 2-20-2024

class Animal:
    has_brain = True
    is_alive = True
    age = 0
    name = None

    def move(speed, direction, distance):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def chirp(self):
        print("""
            __         _____________   
          _/ '>       / CHIRP CHRIP \\
    _ _.-'(   )'-._ _ \\_____________/
   '=._.=-(   )-=._.='    
          |/-\|           
          Y   Y
""")


billy = Bird("Billy", 16)
print(f"This is {billy.name}, he is a {billy.age} years old!")
print(f"Isn't he cute?! Listen to him chirp chirp away~")
billy.chirp()