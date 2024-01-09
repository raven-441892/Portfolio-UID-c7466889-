# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.

student = int(input("Please enter the total number of students: "))  # Get student count
no_of_sweet = int(input("Enter the number of sweets you have in a tub: "))  # Get sweet quantity
no_of_sweet_per_student = no_of_sweet // student  # Calculate sweets per student
remaining_sweet = no_of_sweet % student  # Calculate leftover sweets
if remaining_sweet == 0 or remaining_sweet == 1:  # Check grammar for output
    print(f"Each student gets {no_of_sweet_per_student} sweets with {remaining_sweet} sweet leftover")
else:  
    print(f"Each student gets {no_of_sweet_per_student} sweets with {remaining_sweet} sweets leftover")
