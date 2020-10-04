#Question1 of Task4
def RevStr(SampleStr):
    stringlen=len(SampleStr)
    NewStr=SampleStr[stringlen::-1]
    print(NewStr)
SampleStr=("1234abcd")
RevStr(SampleStr)

#Question2 of Task4
def Func(userStr):
    Ucase=0
    Lcase=0
    for i in range(len(userStr)):
        if (userStr[i].isupper()):
            Ucase=Ucase+1  
        elif (userStr[i].islower()):
            Lcase=Lcase+1
    print("No. of Upper case letters:",Ucase)
    print("No. of Lower case letters:",Lcase)
Func('Miss Gauri Hatode')

#Question3 of Task4
def ElmUnique(list_1):
    list_2=[]
    for i in list_1:
        if i not in list_2:
           list_2.append(i)
    print(list_2)
list_1=[1,2,3,4,4,5,5,1,2,3]
ElmUnique(list_1)

#Question4 of Task 4
x=[i for i in input().split('-')]
x.sort()
print('-'.join(x))

#Question5 of Task 4
UserInput='Hello world \nPractice makes perfect'
print(UserInput.upper())

#Question6 for Task 4
def StrSum(sum):
    num1=str(input("Enter first integer:"))
    num2=str(input("Enter second integer:"))
    print(int(num1)+int(num2))
StrSum(sum)

#Question7 for Task 4
def strlen(str1,str2):
    if len(str1)<len(str2):
        print(str2)
    elif len(str1)==len(str2):
        print(str1)
        print("\n")
        print(str2)
    else:
        print(str1)
str1=input("Enter string 1:")
str2=input("Enter string 2:")
strlen(str1,str2)

#Question8 for Task 4
def squ():
    t=()
    l=list(t)
    for i in range(1,21):
        l.append(i**2)
        t=tuple(l)
    print(t)
squ()

#Question9 of Task 4
def showNumbers(limit):
    for i in limit:
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
limit=range(40,51)
showNumbers(limit)

#Question10 of Task 4
new_list=filter(lambda x:x%2==0,range(1,21))
print new_list

#Question11 of Task 4
new_list=filter(lambda x:x%2==0,range(1,11))
new_list1=map(lambda x:x**2,new_list)
print(list(new_list1))

#Question12 of Task4
try:
    div=5/0
except:
    print("Execption, cannot divide by 0")

#Question13 of Task4
list1=[[1,2,3],[4,5],[6,7,8]]
new_list=lambda x,y:x+y
new_list1=reduce(new_list,list1)
print(new_list1)

#Question14 of Task4
#i
2

#ii
need to define f and x