def main():
    '''CREATING A CLASS AND DISPLAYING THE OBJECTS'''    
    class employee :
        def __init__(self,id,name):
            self.id = id
            self.name = name
        def display(self):
            print(f'Employee Name:{self.name}\nEmployee ID:{self.id}')
    emp1 = employee(56,'John')
    emp1.display() 

    '''DELETING AN OBJECT'''

    print('AFTER DELETING EMP1.ID')
    del emp1.id
    try:
        print(emp1.id)
    except AttributeError:
        print('emp1.id not defined')


if __name__ == '__main__':
    main()