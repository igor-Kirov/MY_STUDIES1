grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def average(List):
    agrs= 0
    for a in List:
        agrs += a
    agrs=agrs/len(List)
    return agrs

List_students= list(students)
agr_students=dict()
if len(students)== len(grades):
    for y in range(len(List_students)):
        agr_students[List_students[y]]= average(grades[y])
print(agr_students)