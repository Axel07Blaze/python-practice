#testing out variable scope
#1
x = 50

def test():
    x=100
    print("inside X:",x)

test() 
print(x)   

#2
name =("axel")

def hello ():
    print("hello",name)

hello()
