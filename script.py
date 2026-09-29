

#  what are the class 

#class are the blue print or desing 


class Student:

    def Hello():
        print("Welcome to the Hello function ")



std_1=Student()
std_1.name="sunny kumar "
std_1.rollNo=154

print(f"===show all information of student 1=== \n name : {std_1.name} \t rollNo :  {std_1.rollNo} \n")

std_2=Student()
std_2.name="Amit kumar"
std_2.rollNo=12


print(f"===show all information of student 2=== \n name : {std_2.name} \t rollNo :  {std_2.rollNo} \n ")

std_3=Student()
std_3.name="Vikash sir "
std_3.id=101


print(f"===show all information of teacher === \n name : {std_3.name} \t rollNo :  {std_3.id} \n ")



 ========  Concept of constructor ======
when a object create then  constructor are all ready call 

class Employee:

    def __init__(self):
        print("hello when obj create i call ")
        

emp1=Employee()
emp2=Employee()
emp3=Employee()


        

    


















