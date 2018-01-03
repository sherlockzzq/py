#!/usr/bin/env python3
from registar import *
import pandas as pd
from pathlib import Path
import pickle

print('Welcome to the Registration System')

school = input('Please enter the name of your institution: ')
while not school:
    print('Please enter a name!')
    school = input('Please enter the name of your institution: ')
domain_name = input('Please enter the domain of your institution: ')

institution = Institution(school, domain = domain_name)


def print_sign():
    print('Please select an option from the following:')
    print('1    Create a course')
    print('2    Schedule a course offering')
    print('3    List course catalog')
    print('4    List course schedule')
    print('5    Hire an instructor')
    print('6    Assign an instructor to a course')
    print('7    Enroll a student')
    print('8    Register a student for a course')
    print('9    List enrolled students')
    print('10   Students registered for a course')
    print('11   Submit student grade')
    print('12   Get student records')
    print('13   Exit')

path = Path('./registration/{}.pkl'.format(school)) #Yunye Xu told me about this helpful tool to save all the information
course_list = {}
print_sign()
choice = input('Please enter your choice: _ ')

while choice != '13':

    if choice == '13':
        break
    elif choice == '1':
        print('Create a course:\nPlease Enter the following information for a course, eg: MPCS, 51042, Python, 100 : ')
        name = ['Department', 'Number', 'Course name', 'Credits'] #list and for-loop input inspired by Rex Zhou
        course_info = []
        for i in name: 
            info = input(i + ": ")
            course_info.append(info)
        course = Course(*course_info)
        institution.add_course(course)
        print("This course has been added!".format())
    
    elif choice == '2':
        print('Scheduling a course offering:\nPlease enter the following information, eg: Python, Section 1, Nick, 2017, Fall:')
        name = ['Course name', 'Section number', 'Instructor', 'YEAR', 'Quarter(Winter, Spring or Fall)']
        course_offering_info = []
        for i in name:
            user_input = input(i + ": ")
            course_offering_info.append(user_input)
        course = None
        for j in institution.course_catalog:
            if j.name == course_offering_info[0]:
                course = j
        if not course :
            print("No such course!")
        else:
            institution.add_course_offering(CourseOffering(course, *course_offering_info[1:]))

    elif choice == '3':
        courses = institution.list_course_catalog()
        print('Institution {} has the following course catalogs:')
        department_list = { x.name : x.department for x in courses }
        num_list = { x.name : x.number for x in courses }
        credits_list = {x.name : x.credits for x in courses}
        d = pd.Series(department_list)
        n = pd.Series(num_list)
        c = pd.Series(credits_list)
        res = pd.DataFrame({'department' : d, 'number' : n, 'credits': c})
        print(res)

    elif choice == '4':
        year = input("Please input a year: ")
        quarter = input("Please input a quarter: ")
        print('Institution has the following courses:')
        courses = []
        for i in institution.course_offering:
            if i.year == year and quarter == i.quarter:
                courses.append(i)
        co = {'section number': [x.section_number for x in courses], 'instructor': [x.instructor for x in courses], 'year':[x.year for x in courses ], 'quarter':[x.quarter for x in courses]}
        res = pd.DataFrame(co)
        res.index = [x.course.name for x in courses]
        print(res)
    
    elif choice == '5':
        print('Hiring new instructor:\nPlease enter the following information: eg: Adam, Shawn, 1980/01/01, adam_shawn')
        name = ['Last name', 'First name', 'Date of Birth', 'Username']
        instructor_info = []
        for i in name:
            user_input = input(i + ": ")
            instructor_info.append(user_input)
        institution.hire_instructor(Instructor(*instructor_info))
    
    elif choice == '6':
        print('Assign instructor to the given course:\nPlease enter the following information: eg: MPCS, 55001, Section 1, 2017, Autumn, adam_shawn')
        name = ['Username', 'Department' , 'Number', 'Section_number', 'Year', 'Quarter']
        info_list = []
        for i in name:
            info = input(i + ": ")
            info_list.append(info)
        name = info_list[0]
        for i in institution.course_offering:
            if info_list[1] == i.course.department and info_list[2] == i.course.number and info_list[3] == i.section_number and info_list[4] == i.year and info_list[5] == i.quarter:
                for j in institution.employed_instructors:
                    if j.username == name:
                        i.instructor = j

    elif choice == '7':
        print('Enrolling a new student:\nPlease enter the following information: eg: Z, ZH, 1995/01/01, ziqingz')
        name = ['last_name', 'first_name', 'date of birth', 'username']
        info_list = []
        for i in name:
            info = input(i + ": ")
            info_list.append(info)
        institution.enroll_student(Student(*info_list))
    
    elif choice == '8':
        print('Register student to a course:\nPlease enter the following information: eg: ziqingz, MPCS, 51042, 1, 2017, Autumn')
        info_list = []
        name = ['Username', 'Department',  'Number', 'Section_number', 'Year', 'Quarter']
        for i in name:
            info = input(i + ": ")
            info_list.append(info)
        name = info_list[0]
        for i in institution.course_offering:
            if info_list[1] == i.course.department and info_list[2] == i.course.number and info_list[3] == i.section_number and info_list[4] == i.year and info_list[5] == i.quarter:
                for j in institution.enrolled_students:
                    if j.username == name:
                        i.register_students(j)

    elif choice == '9':
        students = institution.list_students()
        student = {'email': [i.email for i in institution.enrolled_students],
                    'username': [i.username for i in institution.enrolled_students], 'birthday': [i.date_of_birth for i in institution.enrolled_students], 'credits': [i.credits() for i in institution.enrolled_students]}
        stu = pd.DataFrame(student)
        stu.index = [i.first_name + ' ' + i.last_name for i in institution.enrolled_students]
        print(stu)
    
    elif choice == '10':
        print('Listing registered students for a course: \nPlease provide the following infomation:\neg: MPCS, 51042, 1, 2017, Autumn')
        name = ['Department',  'Number', 'Section_number', 'Year', 'Quarter']
        for i in name:
            info = input(i + ": ")
            info_list.append(info)
        for i in institution.course_offering:
            if info_list[0] == i.course.department and info_list[1] == i.course.number and info_list[2] == i.section_number and info_list[3] == i.year and info_list[4] == i.quarter:
                students = i.registered_students
                print("students are:")
                print(pd.Series(students))
    
    elif choice == '11':
        print('Submitting grade for a student in course.\neg: ziqingz, MPCS, 51042, Section 1, 2017, Autumn, A')
        name = ['Username', 'Department',  'Number', 'Section_number', 'Year', 'Quarter', 'Grade']
        for i in name:
            info = input(i + ": ")
            info_list.append(info)
        name_z = info_list[0]
        for i in institution.course_offering:
            if info_list[1] == i.course.department and info_list[2] == i.course.number and info_list[3] == i.section_number and info_list[4] == i.year and info_list[5] == i.quarter:
                for j in institution.enrolled_students:
                    if j.username == name_z:
                        i.submit_grade(j, name[-1])


    elif choice == '12':
        print('Showing student\'s records. Input username, eg: ziqingz:')
        n = input('Username:')
        for i in institution.enrolled_students:
            if i.username == n:
                print([j.course.name for j in i.list_courses()])
                print('GPA: ' + str(i.gpa()))
                print('Credits: ' + str(i.credits()))
    else:
        print("Please enter the right number!")
    print_sign()
    choice = input('Please enter your choice: _ ')

print('End')



with open(f'./data/{institution.name}.pkl', 'wb') as output:
    pk.dump(institution,output,pk.HIGHEST_PROTOCOL)
del institution

