name = "Dave" # global scope

def greeting(firstname): # local scope
    color = "blue" # only available in local scope
    print(color)
    print(firstname)
    print(name)

def greeting2(): # local scope
    print(name) # no arg defined so takes from global scope

greeting("John")
greeting2()

# print(color) color not available here

def another():
    greeting("Dave")

another()

def another2():
    color = "blue"

    def greeting3(name):
        print(color)
        print(name)
    
    greeting3("Dave")

another2()
