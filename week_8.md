a = 'Pulp Friction'
n = list(a.lower())
print(n)


input_list = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
list_vow = []
list_cons = []
list_sym = []

vowels = 'aeiou'
for char, count in input_list:
    if char in vowels:
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_sym.append((char, count))

print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)


student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'lab': lab_scores,
    'test': test_scores
}

print("student =", student)


student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'lab': lab_scores,
    'test': test_scores
}
count = int(0)
for i in assignment_scores:
    count += 1
for n in lab_scores:
    count += 1
for k in test_scores:
    count += 1
print("student =", count)



student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'lab': lab_scores,
    'test': test_scores
}
avg_assaignment = sum(assignment_scores) / len(assignment_scores)
avg_lab = sum(lab_scores) / len(lab_scores)
avg_score = sum(test_scores) / len(test_scores)
count = int(0)
for i in assignment_scores:
    count += 1
for n in lab_scores:
    count += 1
for k in test_scores:
    count += 1
final = (0.3 * avg_assaignment) + (0.5 * avg_lab) + (0.2 * avg_score)
print("student =", count, final)


from typing import final

student_name = "Adam"
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]

student_name2 = "Kevin"
assignment_scores_2 = [82, 56]
lab_scores_2 = [78.20, 70.2]
test_scores_2 = [70, 60]

student = {
    'name': student_name,
    'assignment': assignment_scores,
    'lab': lab_scores,
    'test': test_scores,
}

student2 = {
    'name': student_name2,
    'assignment': assignment_scores_2,
    'lab': lab_scores_2,
    'test': test_scores_2,
}

avg_assaignment = sum(assignment_scores) / len(assignment_scores)
avg_lab = sum(lab_scores) / len(lab_scores)
avg_score = sum(test_scores) / len(test_scores)
count = int(0)

avg_assaignment2 = sum(assignment_scores_2) / len(assignment_scores_2)
avg_lab2 = sum(lab_scores_2) / len(lab_scores_2)
avg_score2 = sum(test_scores_2) / len(test_scores_2)
count2 = int(0)
for i in assignment_scores:
    count += 1
for n in lab_scores:
    count += 1
for k in test_scores:
    count += 1
for l in assignment_scores_2:
    count2 += 1
for p in lab_scores_2:
    count2 += 1
for q in test_scores_2:
    count2 += 1
final = (0.3 * avg_assaignment) + (0.5 * avg_lab) + (0.2 * avg_score)
final2 = (0.3 * avg_assaignment2) + (0.5 * avg_lab2)

students_scores = {
    student['name']: {
        'assignment': student['assignment'],
        'lab': student['lab'],
        'test': student['test'],
        'final': final
    },
    student2['name']: {
        'assignment': student2['assignment'],
        'lab': student2['lab'],
        'test': student2['test'],
        'final2': final2
    }
}

print(students_scores)
