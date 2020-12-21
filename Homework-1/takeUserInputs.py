def isBool(data): #Is the value in string data type boolean?
    if data == "True" or data == "False":
        return True
    return False

def isFloat(data): #Is the value in string data type float?
    try:
        float(data)
        return True
    except ValueError:
        return False

# 5 pieces of value are taken from the user and stored in the list.
inputs = []
for i in range(5):
    inputs.append(input(f"{i+1}. Value : "))

# Data and data types receive from the user are printed on the screen.
for k, inp in enumerate(inputs):
    print("----------------------------\n{}. Value\n{}".format(k+1,inp))
    if inp.isdecimal():
        print(type(int(inp)))
    elif isFloat(inp):
        print(type(float(inp)))
    elif isBool(inp):
        print(type(bool(inp)))
    else:
        print(type(inp))