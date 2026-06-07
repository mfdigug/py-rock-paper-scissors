name = "Dave" # global scope
count = 1
# don't pollute the global scope 

def greeting(firstname): # local scope
    color = "blue" # only available in local scope
    global count # identifies that we want to use the global variable not creating a local variable
    count += 1
    print(count)
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
