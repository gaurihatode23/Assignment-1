#Question1 of Task 3
Elements=[10,"Gauri",7j+9,12.20]
print(Elements)

#Question2 of Task 3
>>> a=[1,2,3,4,5]
>>> a[:4]
[1, 2, 3, 4]
>>> a[0:-1]
[1, 2, 3, 4]

#Question3 of Task 3
sum-
>>> a[0:-1]
[1, 2, 3, 4]
>>> sum(a)
15
multiply-
a=[1,2,3,4,5]
result = 1
for x in a: 
    result = result * x  
print("Multiplication of the list",result)

#Question4 of Task 3
largest number-
a=[55,31,99,1200,3]
a.sort() 
print("Largest number is:", a[-1]) 

smallest number-
a=[55,31,99,1200,3]
a.sort() 
print("Smallest element is:", a[0]) 

#Question5 of Task 3
b=[1,2,3,4,5,6,7,8,9,10]
for i in b:
    if i%2==0:
        b.remove(i)
print(b)

#Question6 of Task 3
a=range(1,31)
square=[i**2 for i in a]
print(square[:5])
print(square[-5:])

#Question7 of Task 3
main_list=[[1,3,5,7,9,10],[2,4,6,8]]
result = [j for i in main_list for j in i]
final_list=result.pop(5)
print(result)

#Question8 of Task 3
a={1:10,2:20}
b={3:30,4:40}
c={**a,**b}
Print(c)
{1: 10, 2: 20, 3: 30, 4: 40}

#Question9 of Task 3
n= int(input("Enter the number for n: "))
output_dict = {}
for x in range(1, n+ 1):
    output_dict[x]=x*x
print("Output dictonary-", output_dict)

#Question10 of Task 3
input_string1 = input("Enter a list elements separated by comma ")
print("\n")
user_List = input_string1.split()
print("Final list is :", user_List)

#Question11 of Task 3
elements=[1,2,3,4,"Consultadd","Python",2e+3,7j+2,31.2,40.2]

#Question12 of Task 3
userList=range(1,10)
new_list=userList[4:7]
print new_list

#Question13 of Task 3
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#a
x[5][:4]

#b
x[6:8]

#c
x[::2]

#d
x[-1::-1]

#e
x[5][5][0]

#f
x[-1:-1]

#Question14 of Task 3
new=range(1,1000) #Memory allocated for this is more compare for xrange.Range type is a list

new1=xrange(1,1000) #Memory allocated for this is less than range as xrange type is an object

#Question15 of Task 3
a.Accessing tuple is much faster than List
b.Tuple uses less memory compare to list as stored in single block of memory
c.Errors and excption occurs less in tuple than list

#Question16 of Task 3
for i in range(1,101):
    if (i%3==0) and (i%2==0):
        print(i)
    
#Question17 of Task 3
str="This is a new task for Assignment1a e i o u"
rev_str=len(str)
newstr=str[rev_str::-1]
for i in newstr:
    if i in 'aeiou':
        print(i)

#Question18 of Task 3
def evenwords(sentence):
    sentence = sentence.split(' ')
    for i in sentence:
        if len(i)%2==0:
            print(i)
evenwords("Hello my name is Gauri")

#Question19 of Task 3
def resultnumber(numb, x,sum):
    for i in range(0, numb ): 
        for j in range(i + 1, numb ): 
            if (x[i] + x[j] == sum): 
                print(x[i], x[j]) 
sum=8
x=[1,2,3,4,5,6,7,8,9,-1]
numb=len(x)
resultnumber(numb, x,sum)

#Question20 of Task 3
i=1
while i<=5:
    mainlist=range(1,51)
    i=i+1
    even_list=[x for x in mainlist if x % 2 == 0]
    odd_list=[x for x in mainlist if x % 2 != 0]
    new_num=int(input("Enter a number in range of 1 to 50: "))
    if new_num%2==0:
       even_list.append(new_num)
       print("New even list is:",even_list)
       break
    else:
       odd_list.append(new_num)
       print("New odd list is:",odd_list)
       continue
even_list_sum=sum(even_list)
odd_list_sum=sum(odd_list)
print("Maximum out of list is: "max(even_list_sum,odd_list_sum))

#Question21 of Task 3
Elements= "12abcbacbaba344ab"
Elements1=filter(lambda Elements:Elements.isalpha(), "12abcbacbaba344ab")
frequency={}
for i in Elements1:
    if i in frequency:
        frequency[i]+=1
        break
    else:
        frequency[i]=1
print frequency

#Question22 of Task 3
p=(1,2,3,4,5,6,7,8,9,10)
q=[]
for i in p:
    if i%2==0:
        q.append(i)
print (tuple(q))