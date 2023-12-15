def main():
    class Teacher:
        def __init__(self,name):
            self.name = name
        
        def print_job(self):
            print('I am a teacher')
        
        def print_teacher_job(self):
            self.print_job()
            
        def print_name(self):
            print(f'My name is {self.name}')
            self.print_teacher_job()
       

    class Student(Teacher):
        def print_name(self):
            super().print_name()
        def print_job(self):
            print("I am a student")

    class Youtuber(Student):
        def print_name(self):
            super().print_name()
        def print_job(self):
            print("I am a Youtuber")

    stu1 = Teacher("Vinu")
    stu1.print_name()

    stu2 = Student("Anu")
    stu2.print_name()

    stu3 = Youtuber("Karthi")
    stu3.print_name()

if __name__ == "__main__":
    main()