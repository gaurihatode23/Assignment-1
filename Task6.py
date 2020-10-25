#Question1 of Task 6
x=[10,14,20,30,40,50,60,70]
y=list(filter(lambda x: x%3!=0 and x%7==0,x))
print(y)

#Question2 of Task 6
list1=[2,4,6,8,10,12,14]
list2=list(map(lambda x: x*x, list1))
print(list2)

#Question3 of Task 6
str1='United States of America'
str2=list(filter(lambda x: x.isupper(), str1))
print(str2)

#Question4 of Task 6
student=['smith','Jaya','Rayyan']
capital=['CSE','Networking','Operating System']
dict1=dict(zip(student,capital))
print(dict1)

#Question5 of Task 6
Learned about yield, next and geneartors

#Question6 of Task 6
def rev1(input_str):
    strlen = len(input_str)
    for i in range(strlen - 1, -1, -1):
        yield input_str[i]
for char in rev1("Consultadd Training"):
    print(char)

#Question7 of Task 6
def decorators(function):
    def decorators2(a,b):
        print("My arguments are: {0}, {1}".format(a,b))
        function(a,b)
    return decorators2
@decorators
def cities(city1,city2):
    print("Cities are {0} and {1}".format(city1, city2))
cities("Mumbai", "Delhi")

#Question8 of Task 6
Front-end development technologies and companies who use them-
1. Vue.js- goolge, apple, trivago
2. NPM- Linkedin,Netfix,Uber
3. Angular JS- Morgan Stanley, Facebook, Airbnb
4. REACT-GoldmanSaches
5.Flutter-Cryptigraph, Google, alibaba
