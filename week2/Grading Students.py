# Grading Students

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade > 37 and grade % 5 > 2:
            grade += 5 - (grade % 5)
        rounded_grades.append(grade)
    return rounded_grades
