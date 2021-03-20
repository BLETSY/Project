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

