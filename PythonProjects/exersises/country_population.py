population = {
    "China" :143,
    "India" :136,
    "Usa"   :32,
    "Pakistan":21
}
def add():
    country = input("Enter the country name to add: ")
    country = country.capitalize()
    if country in population:
        print("Country already exists in the database. Terminating")
        return
    p = int(input(f"Enter population of {country}: "))
    population[country] = p
    print_all()

def remove():
    country = input("Enter the country name to remove: ")
    country = country.capitalize()
    if country not in population:
        print("Country does not exist in the database. Terminating")
        return
    
    del population[country]
    print_all()
    

def query():
    country = input("Enter the country name to query: ")
    country = country.capitalize()
    if country not in population:
        print("Country does not exist in the database. Terminating")
        return
    
    print(f"Population of {country} = {population[country]} crores")

def print_all():
    for country,p in population.items():
        print(f"{country}==>{p}")

def main():
    op = input("Enter an operation(add,remove,query,printall)\n")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'remove':
        remove()
    elif op.lower() == 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()