y = 5

def set_x (z) :
    x = z
    global a
    x = y
    print("X is:", x)
    a = 7

print ("y before set_x:", y)

set_x(10)

print("y after set_x:", y)
print("a after set_x:", a)