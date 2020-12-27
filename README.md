# GlobalAIHubPythonHomework

Introduction to Python Course - [Global AI Hub Community](https://globalaihub.com/)

## [Homework 1](https://github.com/enesonmez/GlobalAIHubPythonHomework/blob/master/Homework-1/takeUserInputs.py)
Take 5 values from the user and write a program that prints the values you get on the screen. Print the type of values you received in this program on the screen. When using print functions, do not forget to use f-string and format usage in your program. 

## [Homework 2](https://github.com/enesonmez/GlobalAIHubPythonHomework/blob/master/Homework-2/userInformation.py)
The user will be defined. Get the data of this user by input method. Obtain information from user as follow:
* First Name
* Last Name
* Age
* Date of birth (just year)

Pass the user's information to the list and displays the screen using the for loop. Print all user information on the screen.
If she/he is under 18, print "You can't go out because it's too dangerous" on the screen.
If she/he is over 18, print "You can go out to the street." on the screen.

## [Homework 3 (Hangman Game)](https://github.com/enesonmez/GlobalAIHubPythonHomework/blob/master/Homework-3/hangmanGame.py)
You will make **hangman game**. You are free on this assignment. You can set the rules yourself. There is only one thing expected of you. When entering the game, the user's name and for example "welcome john" should be pressed to the screen. When the game is over, exit the game. So let the game end. <br>
Hangman Game Rules
* User has **6** right to guess.
* The user can predict letter or word.
* The user's right to guess decreases with each wrong guess.
* User can predict word, but if wrong, user's right to guess decreases.
* If user say same word or letter what right to guess not change. She/He get warning message.

## [Course Project Assignment](https://github.com/enesonmez/GlobalAIHubPythonHomework/blob/master/Course-Project-Assignment/studentManagementSystem.py)
Create a Simple **Student Management System**: 
* One student must enter their name and surname. 
* A student who enter name and surname correctly should write "Welcome" on the screen with print. The Student has the right to enter his/her name and surname incorrectly 3 times. For more than 3 incorrect entries, the system shuts down and the message "Please try again later" should be printed on the screen. 
* 5 courses should be created and these courses should be kept in a list. All of these lessons should be taken from the user. 
* This student can take a minimum of 3 and a maximum of 5 lessons. 
* This student cannot take less than 3 courses 
* Otherwise, the message "You failed in class" should be returned to the student by using the return statement 
* The student must choose one of these courses and take an exam. Add the grades from this course to a dictionary and keep the student's grades in this dictionary as midterm final and project grades 
    * Example {"midterm": 38 "final": 66 "project' 39} 
* Percentages for grades 
    * Midterm Exam: 30% 
    * Final 50% 
    * Project: 20% 
* Determine a course passing grade according to the grades received. 
    * for notes 
        * If the grade is> 90. the student should get AA 
        * If 70 < grade < 90 BB 
        * If 50 < grade < 70 CC 
        * If 30 < grade < 50 DD 
        * If x < 30, let FF take 
* If the student has received FF he / she should print his / her failure on the screen 