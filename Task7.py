#Question1 of Task 7
class calculate():
    def __init__(self,C,H):
        self.C=C
        self.H=H
    def formula(self,D):
        return ((2*self.C*D)/self.H)**2
        D=int(input("Enter the value of D"))
obj1=calculate(50,30)
Q = obj1.formula(D)
print(Q)

#Question2 of Task 7
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
        def __init__(self,length):
            Shape.__init__(self)
            self.length=length
            self.Shape=0
        def area(self):
            return self.length*self.length
obj1=Square(50)
new_area=obj1.area()
print("Area is:",new_area)

#Question3 of Task 7

class calculate:
 def threeSum(self, input_num):
        input_num, result, i = sorted(input_num), [], 0
        while i < len(input_num) - 2:
            j, k = i + 1, len(input_num) - 1
            while j < k:
                if input_num[i] + input_num[j] + input_num[k] < 0:
                    j += 1
                elif input_num[i] + input_num[j] + input_num[k] > 0:
                    k -= 1
                else:
                    result.append([input_num[i], input_num[j], input_num[k]])
                    j, k = j + 1, k - 1
                    while j < k and input_num[j] == input_num[j - 1]:
                        j += 1
                    while j < k and input_num[k] == input_num[k + 1]:
                        k -= 1
            i += 1
            while i < len(input_num) - 2 and input_num[i] == input_num[i - 1]:
                i += 1
        return result

print(calculate().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

#Question4 of Task 7
1.class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
Output-File "/Users/gaurihatode/reverse_word.py", line 10, in <module>
    main()
  File "/Users/gaurihatode/reverse_word.py", line 9, in main
    print(b.x,b.y)
AttributeError: 'Derived_Test' object has no attribute 'x'
Reason- class Derived_Test doesn not have variable x defined in it. 
To use the oject of Class test the Derived_Test class should have Test.__init__(self).

2.class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y
def main():
    obj = der()
    print(obj.x, obj.y)
main())
Output-File "/Users/gaurihatode/reverse_word.py", line 11
    main())
          ^
SyntaxError: unmatched ')'
Reason- extra paranthese at the calling of main function

3.class A:
def __init__(self,x):
self.x = x
def count(self,x):
self.x = self.x+1
class B(A):
def __init__(self, y=0):
A.__init__(self, 3)
self.y = y
def count(self):
self.y += 1
def main():
obj = B()
obj.count()
print(obj.x, obj.y)
Main()
Output-File "/Users/gaurihatode/reverse_word.py", line 6, in <module>
    class B(A):
  File "/Users/gaurihatode/reverse_word.py", line 16, in B
    main()
  File "/Users/gaurihatode/reverse_word.py", line 13, in main
    obj = B()
NameError: name 'B' is not defined
Reason- The class objects are defined at the class level no inside a method.

4.class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)
def multiply(self, i):
    self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
    def multiply(self, i):
        self.i = 2 * i;
obj = B()

Output-30

#Question5 of Task 7
class time():

    def __init__(self,hours, minutes):
        self.hours=hours
        self.minutes=minutes
    
    def addTime(x1,x2):
        x3=time(0,0)
        if x1.minutes+x2.minutes > 60:
            x3.hours=(x1.minutes+x2.minutes)/60
        x3.hours=x3.hours+x1.hours+x2.hours
        x3.minutes=(x1.minutes+x2.minutes)-(((x1.minutes+x2.minutes)/60)*60)
        return x3
    
    def display_time(self):
        print("Calcuted Time is:",self.hours,"Calculated hours:",self.minutes,"min")
    
    def display_min(self):
        print((self.hours*60)+self.minutes)
k=time(2,50)
l=time(1,20)
j=time.addTime(k,l)
j.display_time()
j.display_min()

#Question6 of Task 7

