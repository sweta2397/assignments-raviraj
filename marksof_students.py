#program to accept marks of 2 students and display them in a sorted manner
m1=int(input("enter marks for student no 1: "))
m2=int(input("enter marks for student no 2: "))
myList=[m1,m2]
myList.sort()
print(myList)