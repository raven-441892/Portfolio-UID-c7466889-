# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.

# Calculate groups and remaining students, and print the output with grammatical considerations
student=int(input("Please enter the total number of student: "))
group_size=int(input("Enter the number of student you need in each group: "))
no_of_group=student//group_size
remaining_student=student%group_size
if remaining_student==0 or remaining_student==1:
    print(f"There will be {no_of_group} groups with {remaining_student} student leftover")
else:    
    print(f"There will be {no_of_group} groups with {remaining_student} students leftover")
