import json, os, time, random

studentPath = "students.json"
coursePath = "courses.json"
gradePath = "grades.json"

class SMS():
    lastName = ""
    firstName = ""
    __jsonStudent = []
    __jsonCourses = []
    __jsonGrades = []
    id = -1

    def __init__(self, *args, **kwargs): # Loads json files into class variables.
        self.__jsonStudent = self.__jsonRead(studentPath)
        self.__jsonCourses = self.__jsonRead(coursePath)
        self.__jsonGrades = self.__jsonRead(gradePath)

    def initialize(self): # Variables are reset during user change.
        self.lastName = ""
        self.firstName = ""
        self.id = -1
    
    def __jsonRead(self,path): # Json file reads. Returns data back.
        try:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                return data if data != "" else []
        except:
            return []

    def __idShow(self,path,data): # Used to determine the student id.
        if os.path.exists(path):
            return data[-1]["id"] if data != [] else -1
        else:
            return -1

    def register(self,firstName,lastName): # Student registration is made. It is saved in the json file and in the __jsonStudent variable.
        student_dict = {"id" : self.__idShow(studentPath,self.__jsonStudent) + 1,
                "firstName": firstName,
                "lastName": lastName
        }
        self.__jsonStudent.append(student_dict)
        with open(studentPath, 'w+', encoding='utf-8') as json_file:
            json.dump(self.__jsonStudent, json_file, ensure_ascii=False)
    
    def login(self,firstName,lastName): # Returns true if the student login process is successful and false if it fails.
        if self.__jsonStudent != []:
            for student in self.__jsonStudent:
                if firstName == student["firstName"] and lastName == student["lastName"]:
                    self.firstName = firstName
                    self.lastName = lastName
                    self.id = student["id"]
                    return True
        else:
            return False
    
    def courseRegister(self,courses): # With the course list taken from the user, it is saved to the json file.
        courses_dict = {"studentId": self.id,
                        "courses": courses
        }
        self.__jsonCourses.append(courses_dict)
        with open(coursePath, 'w+', encoding='utf-8') as json_file:
            json.dump(self.__jsonCourses, json_file, ensure_ascii=False)
    
    def hasCourseRegister(self): # It queries whether there is a course belonging to the logged in user.
        for course in self.__jsonCourses:
            if self.id == course["studentId"]:
                return True, course["courses"]
        return False, None
    
    def takeExam(self, courseName, grades): # Saves the exam results to the json file.
        grades_dict = {"studentId" : self.id,
                "courseName": courseName,
                "grades": grades
        }
        self.__jsonGrades.append(grades_dict)
        with open(gradePath, 'w+', encoding='utf-8') as json_file:
            json.dump(self.__jsonGrades, json_file, ensure_ascii=False)
    
    def hasGradeExam(self, courseName): # Queries whether there is a exam result belonging to the logged in user.
        for grade in self.__jsonGrades:
            if self.id == grade["studentId"] and courseName == grade["courseName"]:
                    return True
        return False
    
    def courseGradeCalculate(self): # calculates the course grade according to the exam grades.
        grade  = dict()
        for gra in self.__jsonGrades:
            if self.id == gra["studentId"]:
                grade[gra["courseName"]] = {
                    "passingGrade" : (gra["grades"]["midterm"] * 30 + gra["grades"]["final"] * 50 + gra["grades"]["project"] * 20) / 100,
                    "allGrades" : gra["grades"]
                }
        return {} if grade == {} else grade

    

def screenClear(): # Pressing a key clears the screen.
    input("Press any button to continue...")
    os.system('cls' if os.name=='nt' else 'clear')

def screenTimeClear(): # Clears the screen after 1 second.
    time.sleep(1)
    os.system('cls' if os.name=='nt' else 'clear')

def coursesPrint(*SMS): # Prints the courses the user has taken on the screen and returns the courses as a list.
    hasCourse, yourcourses = sms.hasCourseRegister()
    if hasCourse:
        for i, yourcourse in enumerate(yourcourses):
            print(str(i+1) + ". " + yourcourse)
        return yourcourses
    else:
        print("You are not enrolled in any course.")
        return []

if __name__ == "__main__":
    sms = SMS()
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        print("""
            1. Register
            2. Login 
            3. Exit
        """)
        choice = input("Please select an action : ")
        if choice.isdigit():
            if int(choice) == 1: # REGISTER (If the student's name and surname is not registered in the system, it will register.)
                first = input("First Name : ").upper()
                last = input("Last Name : ").upper()
                if sms.login(first,last):
                    print("You have a register.")
                else:
                    sms.register(first, last)
                    print("Registration Successful!")
                screenClear()

            elif int(choice) == 2: # LOGIN (If the user enters incorrectly 3 times, it is returned to the upper menu.)
                screenTimeClear()
                for i in range(3):
                    login = sms.login(input("First Name : ").upper(), input("Last Name : ").upper())
                    if login:
                        print("Welcome {} {}".format(sms.firstName,sms.lastName))
                        break
                    else:
                        print("Your remaining right of entry : {}".format((2-i))) if i != 2 else print("Please try again later")
                    screenClear()
                if login: # If logged in, the system screen is shown.
                    while True:
                        screenClear()
                        print("""
                                1. Register for courses
                                2. Look your registered courses
                                3. Take the exam
                                4. View exam grades
                                5. Logout
                        """)
                        choice = input("Please select an action : ")
                        if choice.isdigit(): 
                            if int(choice) == 1: # Register for courses (The student is allowed to take 3 to 5 classes.)
                                hasCourse, _ = sms.hasCourseRegister()
                                if not hasCourse: # If the student has registered courses before, he / she cannot re-enroll.
                                    screenTimeClear()
                                    while True:
                                        choice = input("How many courses do you want to register? (Exit to q): ")
                                        if choice.isdigit():
                                            if int(choice) < 3:
                                                print("You cannot take less than 3 courses. Because you fail in class.")
                                            elif int(choice) > 5:
                                                print("You can register up to 5 courses.")
                                            else:
                                                courses = list()
                                                for i in range(int(choice)):
                                                    courses.append(input("Course Name : ").upper())
                                                sms.courseRegister(courses)
                                                break
                                        if choice.upper() == "Q":
                                            break
                                else:
                                    print("You have courses register.")

                            elif int(choice) == 2: # Look your registered courses
                                coursesPrint(sms)

                            elif int(choice) == 3: # Take the exam.
                                screenTimeClear()
                                lessons = coursesPrint(sms)
                                if len(lessons) != 0: # If there is no course registered in the system, there cannot be an exam.
                                    while True:
                                        choice = input("Please choose a course to take the exam (Exit to q): ")
                                        if choice.isdigit():
                                            if int(choice) > 0 and int(choice) <= len(lessons):
                                                if not sms.hasGradeExam(lessons[int(choice)-1]):
                                                    grades = dict()
                                                    grades["midterm"] = random.randint(0,100)
                                                    grades["final"] = random.randint(0,100)
                                                    grades["project"] = random.randint(0,100)
                                                    sms.takeExam(lessons[int(choice)-1],grades)
                                                    print("Your exam has taken place. You can see your course grade on the system.")
                                                else:
                                                    print("You have taken the exam for this lesson before. You can then take another exam.")
                                                break
                                        if choice.upper() == "Q":
                                            break

                            elif int(choice) == 4: # View exam grades
                                grade = sms.courseGradeCalculate()
                                if grade != {}:
                                    for keys, values in grade.items():
                                        print(keys.upper())
                                        for key, value in values["allGrades"].items():
                                            print(key.upper() + " : " + str(value))
                                        print("Average : " + str(values["passingGrade"]))
                                        if values["passingGrade"] >= 90:
                                            print("Course passing grade : AA")
                                        elif values["passingGrade"] >= 70 and values["passingGrade"] < 90:
                                            print("Course passing grade : BB")
                                        elif values["passingGrade"] >= 50 and values["passingGrade"] < 70:
                                            print("Course passing grade : CC")
                                        elif values["passingGrade"] >= 30 and values["passingGrade"] < 50:
                                            print("Course passing grade : DD")
                                        else:
                                            print("Course passing grade : FF")
                                            print("You failed the course.")
                                        print("-" * 50)
                                else:
                                    print("You do not have an exam grade.")

                            elif int(choice) == 5: # LOGOUT
                                sms.initialize()
                                break
                            else:
                                continue

            elif int(choice) == 3: # EXIT
                exit(1)
            else:
                continue