#This program are only for variable 
Name="kamal pankaj"
print(Name)
print("Name is a variable that is hold kamal pankaj")

#Local Variable
print("Local Variable Example: ")
def Mydetails():
    MyName="Kamal Pankaj" # Local Variable
    MyAddress="Gachibowli Hyderabad" # Local Variable
    print(MyName)
    print(MyAddress)
Mydetails()

#Globle Varibale
print("Global Variable Exxample: ")
MyName="Kamal Pankaj" #Global Variable
def MyDetails():
    MyAddress="Gachibowli Hyderabad"#Local Variable
    print(MyName)
    print(MyAddress)
MyDetails()
