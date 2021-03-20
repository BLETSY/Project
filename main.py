import math

x= [4,1,2,3,4,5]

y= x[2]
print (y)
x.append(6)
print (x)
t=x.index(4)
print(t)
x.remove(1)
print(x)
s=x.copy()
print(s)
s.remove(3)
print(s)
print(x)
s.copy()

# 2 Values
# True or False
age = 20
is_the_student_old = age > 18

if is_the_student_old:
    print("You are older than a senior in high school")
my_string="abcd"
my_boolean = 3 in x

print(my_boolean)


# Make a list of names that has 5 names
# Make a variable called has_jimmy and this 
# variable is going to check if the student with 
# the name "Jimmy" is in the list


my_list = ["Sarah", "Christian", "Jimmy", "Michael"]
has_Jimmy = "Jimmy" in my_list

if has_Jimmy:
    print("Jimmy is already in the list")
else:
    my_list.append ("Jimmy")    


def add(x, y):

    x = x ** 5
    y = y ** 5
    return x+y

# distance
# x1, y1, x2, y2
# User distance formula to 
# calculate the distance between these 2 point
# d = math.sqrt((x1-x2)^2 + (y1-y2)^2)
def d(x1, y1, x2, y2):
  d= math.sqrt(((x1 - x2)**2) + (y1-y2)**2)
  return d

x1 = 5
y1 = 10
x2 = 4
y2 = 8
distance = d(x1, y1, x2, y2)
print(distance)


# x = (x1 + x2) / 2
def m(x1, y1, x2, y2):
  mx= (x1+x2)/2
  my= (y1+y2)/2
  return (mx, my)
  
x1=4
x2=5
y1=3
y2=7
midpoint= m(x1, y1, x2, y2)
print (midpoint)

def make_list_empty(l):
    l.clear()

make_list_empty(x)

print(x)

def is_student_old(age):
    return age > 22

if is_student_old(19):
    print("You are older than a high school student")

if is_student_old(24):
    print("You are older than a college studnet")