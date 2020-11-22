from statistics import mean
from dataclasses import dataclass
from typing import List
from random import randint
import json

@dataclass
class Student:
    name: str
    surname: str
    grades: dict
    presences: dict

    def add_new_grade(self,grade,subject_name):
        self.grades[subject_name].append(grade) 

    def calculate_avg(self, subject_name):
        return mean(self.grades[subject_name])
    
    def calculate_presence(self, subject_name):
        return mean(self.presences[subject_name]) * 100
    
    def append_subject_name(self, subject_name):
        if subject_name not in self.grades and subject_name not in self.presences:
            self.grades[subject_name] = []
            self.presences[subject_name] = []
    
    
@dataclass
class Subject:
    subject_name: str
    list_of_students: List[Student]

    def add_student(self, student):
        student.append_subject_name(self.subject_name)
        self.list_of_students.append(student)

    def add_presence(self, presence, student):
        if presence == 'present':
            student.presences[self.subject_name].append(1)
        elif presence == 'absent':
            student.presences[self.subject_name].append(0)

    def avg_grade_for_every_student(self):
        result = list(map(lambda x: mean(x.grades[self.subject_name]), self.list_of_students))
        return result

@dataclass
class School:
    school_name: str
    list_of_subjects: List[Subject]

    def add_subject(self, subject):
        self.list_of_subjects.append(subject)

    def get_all_grades(self):
        all_grades = []
        for subjects in self.list_of_subjects:
            for student in subjects.list_of_students:
                all_grades.append(student.grades[subjects.subject_name])
        return all_grades

    def get_students_names(self):
        ret_list = []
        for subject in self.list_of_subjects:
            for student in subject.list_of_students:
                ret_list.append(student.name)
        return ret_list


def rand_list(length, min_value, max_value):
    return_list = []
    for i in range(1, length):
        return_list.append(randint(min_value, max_value))
    return return_list

def find_student(searched_student, schools):
    found_schools = []
    found_subjects = []
    for school in schools:
        for subject in school.list_of_subjects:
            for student in subject.list_of_students:
                if student.name == searched_student.name and student.surname == searched_student.surname:
                    found_schools.append(school.school_name)
                    found_subjects.append(subject.subject_name)
    return {"schools" : found_schools, "subjects": found_subjects}

def store_to_json(object_to_store, file_name):
    diction = {}
    diction[object_to_store.school_name] = []
    index = 0
    for subject in object_to_store.list_of_subjects:
        diction[object_to_store.school_name].append({'subject' : subject.subject_name, 'students' : []})
        for student in subject.list_of_students:
            diction[object_to_store.school_name][index]['students'].append(student.__dict__)
        index += 1
    with open('{}.json'.format(file_name), 'w') as fp:
        json.dump(diction, fp, indent=4)
    
    
if __name__ == '__main__':

    students = []
    school1 = School('school1', [])
    school2 = School('school2', [])
    schools = [school1, school2]

    math = Subject('math', [])
    physics = Subject('physics', [])
    pe = Subject('pe', [])

    school1.add_subject(math)
    school1.add_subject(physics)
    school2.add_subject(pe)
    
    for i in range(0,12):
        students.append(Student("name{}".format(i),"surname{}".format(i), {}, {}))
        subj_name = ''
        rand_num = randint(0,2)
        if rand_num == 0:
            subj_name = 'math'
            math.add_student(students[i])
        elif rand_num == 1:
            subj_name = 'physics'
            physics.add_student(students[i])
        else:
            subj_name = 'pe'
            pe.add_student(students[i])
        students[i].grades[subj_name] = rand_list(8,1,5)
        students[i].presences[subj_name] = rand_list(5,0,1)

    math.add_student(students[0])
    students[0].grades[math.subject_name] = rand_list(8,1,5)
    students[0].presences[math.subject_name] = rand_list(5,0,1)
    print('avarage of {} student in the {} class: {}'.format(students[0].name, math.subject_name, students[0].calculate_avg(math.subject_name)))
    print('presence of {} student in the {} class: {}'.format(students[0].name, math.subject_name, students[0].calculate_presence(math.subject_name)))
    print('find students {} school: {} and subjects: {}'.format(students[2].name, find_student(students[2], schools)['schools'], find_student(students[2], schools)['subjects']))
    print('avarage grade for every student in math class: {}'.format(math.avg_grade_for_every_student()))
    print('get all grades of students from shchool: {}'.format(school2.get_all_grades()))
    print('get name of every student : {}'.format(school2.get_students_names()))

    store_to_json(school1, 'school1')