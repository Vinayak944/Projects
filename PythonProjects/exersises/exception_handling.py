def main():
    class AdultException(Exception):
        pass

    class Person:
        def __init__(self,name,age):
            self.name = name
            self.age =age
        def is_minor(self):
            if self.age >= 18:
                raise AdultException
            else:
                return self.age
        def display(self):
            try:
               print(f'age -> {self.is_minor()}')
            except AdultException:
                print("You are an Adult")
            finally:
                print(f'name -> {self.name}')
    
    per = Person('Vinu',17)
    per.display()

if __name__ == "__main__":
    main()