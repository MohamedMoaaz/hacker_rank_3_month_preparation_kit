# Grading Students

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade > 37 and grade % 5 > 2:
            grade += 5 - (grade % 5)
        rounded_grades.append(grade)
    return rounded_grades

# more pyhtonic 

def gradingStudents(grades):
    return [grade if grade < 38 or grade % 5 < 3 else grade + 5 - (grade % 5) for grade in grades]
