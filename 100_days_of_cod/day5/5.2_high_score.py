student_scores = input('Inpout a list of estudents scores ').split(', ')
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)
    
high = 0
for student in student_scores:
    if student > high:
        high = student

print(f'The highest score in the class is: {high}')
