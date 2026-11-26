#iniciamos variables

total_passing_grades = 0
total_failed_grades = 0
average_all_grades = 0
average_passing_grades = 0
average_failed_grades = 0
notes_counter = 1
notes_passing_counter = 0
notes_failed_counter = 0
name = input("Ingrese su Nombre:")
total_notes = int(input("Ingrese la cantidad de Notas: "))

#Usuario ingresa las notas una por una y se evalua la condicion < 70
#se suma la nota al total global y a cada caso segun aprobada o desaprobada
#se aumenta en uno el contador
while notes_counter <= total_notes:
     actual_note = int(input(f"Ingrese la Nota #{notes_counter}: "))

     if actual_note < 70:
          total_failed_grades = total_failed_grades + 1
          average_failed_grades = average_failed_grades + actual_note
          average_all_grades = average_all_grades + actual_note
          notes_failed_counter = notes_failed_counter + 1
          notes_counter = notes_counter + 1
          
     else:
          total_passing_grades = total_passing_grades + 1
          average_passing_grades = average_passing_grades + actual_note
          average_all_grades = average_all_grades + actual_note
          notes_passing_counter = notes_passing_counter + 1
          notes_counter = notes_counter + 1

#promedio de notas global
average_all_grades = average_all_grades /  total_notes   

#promedio de notas aprobadas
#en caso de todas aprobadas, proteger la division con 0
if notes_passing_counter==0:
     average_passing_grades=0
else:
     average_passing_grades = average_passing_grades / notes_passing_counter 


#promedio de notas desaprobadas
#en caso de todas desaprobadas, proteger la division con 0
if notes_failed_counter==0:
     average_failed_grades=0
else:
     average_failed_grades = average_failed_grades / notes_failed_counter 

#mostrar los resultados al estudiante
print (f"El estudiante tiene esta cantidad de notas aprobadas: {notes_passing_counter}")  
print (f"Este es el promedio de notas aprobadas: {average_passing_grades}")    

print (f"El estudiante tiene esta cantidad de notas desaprobadas: {notes_failed_counter}")  
print (f"Este es el promedio de notas desaprobadas: {average_failed_grades}") 

print (f"El estudiante tiene esta cantidad de notas cursadas en el año: {total_notes}")  
print (f"Este es el promedio total de notas: {average_all_grades}") 