def division():
    student_name = input("Name of student: ")
    gpa = float(input("Current gpa: "))

    if gpa >= 3.6:
        division = "First Class"
    elif gpa >= 3.0 and gpa <= 3.5:
        division = "Second Class Upper"
    elif gpa >= 2.5 and gpa <= 2.9:
        division = "Third Class"
    elif gpa >= 2.0 and gpa <= 2.4:
        division = "Third Class"
    else:
        division = "Pass"
    print(f"{student_name} is in {division}")

division()