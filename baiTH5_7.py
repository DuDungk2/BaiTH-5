import numpy as np
data_type=[('name','S15'),('class', int),('height',float)]
students_dentails=[('Jame',5,48.5),('Nail',6,52.2),('Paul',5,42.10),('Pit',5,40.11)]
students= np.arry(students_dentails, dtype= date_type)
print('Original array:')
print(sutdents)
print('Sort by height')
print(np.sort(students,ordef='height'))
