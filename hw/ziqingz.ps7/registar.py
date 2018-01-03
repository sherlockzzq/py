class Course():
    def __init__(self, department, number, name, credits):
        self.department = department
        self.number = number
        self.name = name
        self.credits = credits


class CourseOffering():
    def __init__(self, course, section_number, instructor, year, quarter):
        self.course = course
        self.section_number = section_number
        self.instructor = instructor
        self.year = year
        self.quarter = quarter
        self.registered_students = []
        self.grades = {}

    def register_students(self, *students):
        for student in students:
            if student in self.registered_students:
                print('{} is already registered for this course!'.format(student.username))
            else:
                self.registered_students.append(student)
                print('{} registered to course successfully!'.format(student.username))

    def get_students(self):
        if len(self.registered_students) == 0:
            print('No student has registered yet!')
        return self.registered_students

    def submit_grade(self, student, grade):
        if student not in self.registered_students:
            for st in self.registered_students:
                if student == st.username:
                    self.grades[student] = grade
        else:
            if type(student) == Student:
                self.grades[student.username] = grade


    def get_grade(self, student):
        try:
            if type(student) == Student:
                return self.grades[student.username]
            else:
                return self.grades[student]
        except:
            print('no such key')


    """
    def __gt__(self, other):
        if self.year != other.year:
            return self.year > other.year
        else:
            if self.quarter == 'Fall' and other.quarter != 'Fall':
                return True
            elif self.quarter == 'Spring' and other.quarter == 'Winter':
                return True
            else:
                return False

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        else:
            if self.quarter == 'Winter' and other.quarter != 'Winter':
                return True
            elif self.quarter == 'Spring' and other.quarter == 'Fall':
                return True
            else:
                return False
    def __eq__(self, other):
        if self.year == other.year and self.quarter == other.quarter:
            return True
        else:
            return False
    """


class Institution():
    def __init__(self, name, domain = None):
        self.name = name
        self.domain = domain
        self.enrolled_students = []
        self.hired_instructors = []
        self.course_catalog = []
        self.course_offering = []

    def list_students(self):
        if len(self.enrolled_students) == 0:
            print('No student has enrolled yet!')
        return self.enrolled_students

    def enroll_student(self, student):
        if student in self.enrolled_students:
            print('{} already enrolled!'.format(student))
        else:
            self.enrolled_students.append(student)
            student.school = self
            print('{} enrolled successfully!'.format(student))

    def list_instructors(self):
        if len(self.hired_instructors) == 0:
            print('No student has enrolled yet!')
        return self.hired_instructors

    def hire_instructor(self, instructor):
        if instructor in self.hired_instructors:
            print('instructor {} already hired!'.format(instructor))
        else:
            self.hired_instructors.append(instructor)
            instructor.school = self
            print('Hire {} successfully'.format(instructor))

    def list_course_catalog(self):
        if len(self.course_catalog) == 0:
            print("No course offered")
        return self.course_catalog

    def list_course_schedule(self, year, quarter, department=None):
        offering = self.course_offering
        res = []
        for course_offered in offering:
            if department:
                if course_offered.year == year and course_offered.quarter == quarter and course_offered.course.department == department:
                    res.append(course_offered)
            else:
                if course_offered.year == year and course_offered.quarter == quarter :
                    res.append(course_offered)
        return res

    def add_course(self, course):
        if course in self.course_catalog:
            print('Course already exists!')
        else:
            self.course_catalog.append(course)

    def add_course_offering(self, courseoffering):
        if courseoffering.course in self.course_catalog:
            self.course_offering.append(courseoffering)
        else:
            print('Please add course {} first!'.format(courseoffering.course.name))

    def __str__(self):
        return self.name


class Person():
    def __init__(self, last_name, first_name, date_of_birth):
        self.last_name = last_name
        self.first_name = first_name
        self.school = None
        self.usename = None
        self.date_of_birth = date_of_birth
        self.affiliation = None

    @property
    def email(self):
        if not self.school:
            self.email = (self.username + '@' + self.school.domain)

    def __str__(self):
        return self.username


class Instructor(Person):
    def __init__(self, last_name, first_name, date_of_birth, username):
        Person.__init__(self, last_name, first_name, date_of_birth)
        self.username = username
        self.affiliation = 'instructor'

    def list_courses(self, year=None, quarter=None):
        course_teach = []
        for offered_course in self.school.course_offering:
            if offered_course.instructor.username == self.username:
                if offered_course.year == year if year else True:
                    if offered_course.quarter == quarter if quarter else True:
                        course_teach.append(offered_course)
        course_teach = sorted(course_teach, key=lambda course: (course.year, course.quarter), reverse=True)
        return course_teach

    def __str__(self):
        return self.username


GRADE = {'A+': 4, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7, 'C+': 2.3, 'C': 2, 'C-': 1.7, 'D+': 1.3, 'D': 1,'D-': 0.7, 'F': 0}


class Student(Person):
    def __init__(self, last_name, first_name,date_of_birth, username):
        Person.__init__(self, last_name, first_name, date_of_birth)
        self.username = username
        self.affiliation = "student"

    def list_courses(self):
        course_taken = []
        for course in self.school.course_offering:
            if self in course.registered_students:
                course_taken.append(course)
        course_taken = sorted(course_taken, key=lambda course: (course.year, course.quarter), reverse=True)
        return course_taken

    def credits(self):
        credits = 0
        list_courses = self.list_courses()
        for course_taken in list_courses:
            credits += int(course_taken.course.credits)
        return credits

    def gpa(self):
        list_courses = self.list_courses()
        total_grade = 0
        for course in list_courses:
            try:
                grade = course.get_grade(self.username)
                credit = int(course.course.credits)
                total_grade += GRADE[grade] * credit
            except:
                continue
        credit =  self.credits()
        try:
            return total_grade / credit
        except ZeroDivisionError:
            return 0
            print("Credit is zero!")


    def __str__(self):
        return self.username


