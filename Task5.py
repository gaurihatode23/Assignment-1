#Question1 of Task 5
try:
    sum=5+'Consultadd'
except:
    print("Syntax Error")


#Question3 of Task 5
while True:
    try:
        n =input("Please enter an integer: ")
        if len(n)>4 or len(n)<4:
            raise ValueError
    except:
        print("Please length is too short/logn!!! Please provide only four digits")
    else:
        print("Number is accepted")

#Question4 of Task 5
for i in range(3):
    try:
        username = eval(input("Please enter the user name: "))
        password= eval(input("Please enter the password: "))
        re_enter_password= eval(input("Please re-enter the password: "))
        if password!=re_enter_password:
            raise ValueError
        else:
            print("Account is successfully created")
            break
    except:
        print("Incorrect password. Please try again")

#Question6 of Task 5
x=open('file1.txt','r')
data=x.readlines()
for i in data:
    word=i.split(' ')
    for j in words:
        if(len(j%2==0)):
            print (j)