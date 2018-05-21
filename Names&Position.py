# -*- coding: utf-8 -*-
"""
Created on Sun May 20 2018

@author: Edward Moon
"""
class E3:
    
    empCount = 0

    #User defined function here
    def __init__(self, name, role):
            self.name = name
            self.role = role
            E3.empCount += 1

    #Display the parameters
    def displayE3(self):
        #Call the displayE3 function
         print('Name: ', self.name, ', Role: ', self.role)


#Ask for user input
choice = input(str('Would you like to see the contents? Y or N: '))
if choice == 'y':
            print('Lets take a look!')
elif choice == 'n':
            print("Never mind then not interested..")
            exit() #exit out of program when user types 'n'

#Here is where the name and roles will be printed
print("----------NAMES & POSITIONS------------")

em1 = E3("Edward", "Tech Guy")
em2 = E3("Jonathan", "Administrator at Data Center")
em3 = E3("Andrew", "Human Resources")
em4 = E3("Nicole", "Nurse")
em5 = E3("Elizabeth", "Actress")
em6 = E3("Jason", "Accountant")
em7 = E3("Helen", "Attorney")
em8 = E3("Seungi", "Singer")
em9 = E3("David", "Data Analyst")
em10 = E3("Vince", "Professional Muay Thai Fighter")

#Display E3
em1.displayE3()
em2.displayE3()
em3.displayE3()
em4.displayE3()
em5.displayE3()
em6.displayE3()
em7.displayE3()
em8.displayE3()
em9.displayE3()
em10.displayE3()

#Print out total of employees
print("Total number of Employees: ", E3.empCount)
