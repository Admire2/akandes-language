# Simple interpreter for .chips files (Python-like subset)
def run_chips_file(filename: str):
    with open(filename, 'r') as f:
        code = f.read()
    # For now, just execute as Python (for demo purposes)
    exec(code, {})

def greet(name):
    print('Hello,', name)
greet('Akande')

for i in range(5):
    print('Number:', i)

x = 10
if x > 5:
    print('x is greater than 5')
else:
    print('x is 5 or less')

class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello, my name is', self.name)
p = Person('Akande')
p.say_hello()

squares = [x * x for x in range(1, 6)]
print('Squares:', squares)


