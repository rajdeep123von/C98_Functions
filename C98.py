f = open("test.txt")
fileLine = f.readlines()
for line in fileLine:
    print(line)

introString = "My name is Rajdeep. I am learning python"
words = introString.split(".")
print(words)

def greet(name):
    print("Hello!"+name)

greet("raj")

