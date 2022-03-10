from .models import Department, Student

def studentHandler(user, payload):
    #compile the full name of the user
    fullname = payload.get('first_name') + payload.get('last_name')
    #Create the new student
    student = Student(name = fullname, id= payload.get('id_no'), phone= payload.get('phone'))
    #link the user to the student
    student.user = user
    #link the department to the
    student.department = Department.objects.all().filter(department=payload.get('department'))
    #save the record
    student.save()
    #return
    return


def staffHandler():
    pass