#Question1 of Task2
a=30
b=5
d=15
if a/3:
    print("Consultadd")
if b/5:
    print("c")
if d/3 and d/5:
    print("Consultadd ython Training")

#Question2 of Task2
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=0
Result=input("Enter any number from 1-5 for +,-,/,*,Avg accordingly")
if Result== 1:
   z=x+y
elif Result== 2:
     z=x-y
elif Result== 3:
     z=x/y
elif Result== 4:
     z=x*y
elif Result== 5:
     z=(x+y)/2
else:
    print("Input int not found in the list")

 first=int(input("Enter first number:"))
 second=int(input("Enter second number:"))
 z=0
 Result=int(input("Enter 5 for avg"))
 if Result==5:
    z=(first+second)/2
    if z < 0:
     print ("Negative")
    else:
     print("Positive")
  else:
     print("Invalid input")
  print(z)

#Question3 of Task2
a=10
b=20
c=30
Avg=((a+b+c)/3)
print("Average",Avg)
if Avg>a and Avg>b and Avg>c:
    print("Aberage is higher than a,,b,c")
if Avg>a and Avg>b:
    print("Average is higher than abc")
elif Avg>a and Avg>c:
    print("Average is higher than a,c")
elif Avg>a:
    print("Average is just higher than a")
elif Avg>b:
    print("Average is just higher than b")
elif Avg>c:
    print("Average is just higher than c")  

#Question4 of Task2
while True:
    a=int(input("Enter the number of your choice"))
    if a<0:
       print("It's Over")
       break
    if a>0:
       print("Good Going")
       continue

#Question5 of Task2
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        print(x)

#Question6 of Task2
1) x=123
for y in x:
    print(y)
answer- This throws TypeError:'int'object is not iterable as integers can't be iterable in pythong only variable with type list, tuple, strig can be iterable.

2)
i=0
while i<5: # start the while loop as conditoon is true
    print(i) 
    i+=1 # i is 0 so i=i+1 is 1 do this until i=2 and go to else
    if i==3 #jump out of the loop
    break
    else:
        print("Error")
Answer-The output is 
0 
error
1
error
2

3) count=0
while True: # while condition is true so get into the loop
    print(count) #print current number of count
    count+=1 #perform count=count+1
    if count>=5: # jump out of the loop and stop pritning when count is grater than or equals 5
        break
Answer- The output for this is 
0
1
2
3
4


#Question7 of Task2
x=[0,1,2,3,4,5,6]
for val in x:
    if val!=3 and val!=6:
        print(val)
    else:
        continue

#Question8 of Task2
string = input("Enter the input string:")
d=0
l=0
for c in string:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
        
#Question 9.1 of Task2
while True:
    x = int(input("Guess the lucky number:"))
    luckynum=100
    if x==luckynum:
        break
    else:
        continue

#Question 9.2 of Task2
while True:
    x = int(input("Guess the lucky number:"))
    number=100
    if x==number:
        break
    else:
        answer=str(input("Want to guess again? Yes/No"))
        if answer=='Yes':
           continue
        else:
            break

#Question10 of Task2
counter=1
guess=int(input("enter your guess"))
number=100
while counter<=5:
    print("you have guessed",counter,"number:",guess)
    counter=counter+1
    if guess==number:
        print("Good guess!")
    else:
        print("Game over!")


