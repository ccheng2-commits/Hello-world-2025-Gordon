## I use Phython to greet the user and display the current date.
## use the datetime module to get the current date.
## know how to use input() to get user input.
## know how to use print() to display output.
## know how to use daytime.date.today() to get the current date.


import datetime
person = input('Enter your name: ')
day = datetime.date.today()
print('Hello', person, "today is", day) 
