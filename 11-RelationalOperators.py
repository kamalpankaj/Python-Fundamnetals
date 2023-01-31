#In this prrogram Only for Operators
#2.Relational Operators in Python
Num1=None
Num2=None
Result=None
print("1.Program we are checking First Number & Second Number is Equal or Not")
print("2.Program we are checking First Number & Second Number is Not Equal or Equal")
print("3.Program we are checking First Number & Second Number is Less than or equal to")
print("4.Program we are checking First Number & Second Number is Greater than or equal to")
print("5.Program we are checking First Number & Second Number is Greater than")
print("6.Program we are checking First Number & Second Number is Less than")
print("7.Program we are checking first number & second number is same")
print("8.Program we are checking first number & second number is not same")

Num1=input('Please Enter Fisrt Number: ')
Num1=int(Num1)
Num2=input('Please Enter Second Number: ')
Num2=int(Num2)

# Equal Operators
Result=Num1==Num2
print("Result is: "+str(Result))
# Not Equal Operators
Result=Num1!=Num2
print("Resualt is: "+str(Result))
#Less than or equal to
Result=Num1<=Num2
print("Result is: "+str(Result))
#Greater than or equal to
Result=Num1>=Num2
print("Result is: "+str(Result))
#Greater than
Result=Num1>Num2
print("Result is: "+str(Result))
#Less than
Result=Num1<Num2
print("Result is: "+str(Result))
# is 
Result=Num1 is Num2
print("Result is: "+str(Result))
# is not
Result=Num1 is not Num2
print("Result is: "+str(Result))
