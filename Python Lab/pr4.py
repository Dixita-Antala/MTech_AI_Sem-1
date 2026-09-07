# If statement

standard = 10

if standard == 10:
    print("You are in 10th standard.")

# If else statement

age = 20

if age >= 18 :
    print("You can drive.")
else :
    print("You are below the 18, so you can't drive.")

# Nested If

marks = 92

if marks >= 35 :
    if marks >= 35 and marks <= 60:
        print("You passed the exam with Grade E")
    elif marks > 60 and marks <= 70:
        print("You passed the exam with Grade D")
    elif marks > 70 and marks <= 80:
        print("You passed the exam with Grade C")
    elif marks > 80 and marks <= 90:
        print("You passed the exam with Grade B")
    elif marks > 90 and marks <= 100:
        print("You passed the exam with Grade A")
else :
    print("You failed the exam.")