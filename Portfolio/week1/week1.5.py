# 5. The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group

#divides the student into groups
number=int(input("Enter number of students: "))
group=int(number/24)
leftover=number%24
print(f"In {number} students there will be {group} groups and {leftover} students in smaller group")