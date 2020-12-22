# Dictionary data type can be used instead of two lists.
user = list()
parameters = list(["First Name","Last Name","Age", "Date of birth (just year)"]) 

# User information is retrieved.
for i in range(4):
    user.append(input(parameters[i] + " : "))
    # If the age data is not a number, the user is asked to enter a number.
    if i == 2 and not user[i].isdecimal(): 
        while True:
            age = input("Age (please enter number) : ")
            if age.isdecimal():
                user.insert(2,age)
                break

print("----------------------------------")
# User data is printed on the screen.
for param, value in zip(parameters,user):
    print(param + " : " + value)

print("You can't go out because it's too dangerous") if int(user[2]) < 18 else print("You can go out to the street.")