def main():
    # List String Variable if
    # https://github.com/codebasics/py/tree/master/Basics/Exercise

    #Variable

    # byear = 1994
    # cyear = 2023
    # print(cyear - byear)
    # first = "Vinayak"
    # last = " Ganesh"
    # print(first + last)

    # ffl = 92
    # ffw = 48.8
    # print("area = ", round(ffw*ffl,2))

    # qua = 9
    # cost = 1.49
    # cashed = 20
    # bal =  cashed - (qua*cost)
    # print(bal)

    # side = 5.5
    # cost = 500
    # total_cost = side**2 * cost
    # print(total_cost) 

    # number = 17
    # binary = bin(number)
    # print(binary[2:])

    #String

    # street = "Baker Street"
    # city = "London"
    # country = "England"
    # print(f"{street}\n{city}\n{country}")

    # str = "Earth revolves around the sun"
    # print(str[6:13])
    # print(str[-3:])

    # s = "I ate 200 bananas"
    # print(s.replace("200 bananas","10 sandwiches"))

    #List

    # monthly_expenses = [2200,2350,2600,2130,2190]
    # print("Monthly Expense:", monthly_expenses)
    # extra_exp = monthly_expenses[1]-monthly_expenses[0]
    # total_exp_first_quarter = sum(s for s in monthly_expenses[:3] )
    # monthly_expenses.append(1980)
    # monthly_expenses[3] -= 200
    # print('Extra expenses for the month of Feb:', extra_exp, '\nTotal expense for first quarter: ',total_exp_first_quarter,'\nUpdated Monthly Expense:',monthly_expenses)

    # heros=['spider man','thor','hulk','iron man','captain america']
    # print(f"Length of the list:{len(heros)}\n")
    # heros.append('black panther')
    # print("Updated list: ", heros)
    # heros.pop()
    # print("Updated list: ", heros)
    # heros.insert(3,'black panther')
    # print("Updated list: ", heros)
    # heros[1:3]= ["doctor strange"]
    # print("Updated list: ", heros)
    # heros.sort()
    # print(heros)

    # if

    # india = ["mumbai", "banglore", "chennai", "delhi"]
    # pakistan = ["lahore","karachi","islamabad"]
    # bangladesh = ["dhaka", "khulna", "rangpur"]
    # inp = input("Enter the city name: ").lower()
    # if inp in india:
    #     print("India")
    # elif inp in pakistan:
    #     print("Pakistan")
    # elif inp in bangladesh:
    #     print("Bangladesh")
    # else:
    #     print("City name not found on any list")
    # cities = []
    # for _ in range(2):
    #     city = input("Enter city name: ").lower()
    #     cities.append(city)
    # print(cities)
    # if cities[0] in india and cities[1] in india:
    #     print('India')
    # elif cities[0] in pakistan and cities[1] in pakistan:
    #     print("Pakistan")
    # elif cities[0] in bangladesh and cities[1] in bangladesh:
    #     print("Bangladesh")
    # else:
    #     print("Both cities are not in the same country")

    # for i in range(2):
    #     if city[i] and city[i+1] in india:
    #         print('India')
    #     elif city[i] and city[i+1] in pakistan:
    #         print("Pakistan")
    #     elif city[i] and city[i+1] in bangladesh:
    #         print("Bangladesh")
    #     else:
    #         print("Both cities are not in the same country")
        
    # fasting_sugar = int(input("Enter your fasting sugar level: "))
    # if fasting_sugar <80:
    #     print("Sugar level is low")
    # elif fasting_sugar > 100:
    #     print("Sugar level is high")
    # else:
    #     print("Sugar level is normal")

    # for

    # result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    # count = 0
    # for r in result:
    #     if r == 'heads':
    #         count += 1
    # print("Number of heads: ", count)

    # for i in range(1,10,2):
    #     s = (i)*(i)
    #     print((s))

    # expense_list = [2340, 2500, 2100, 3100, 2980]
    # month_list = ["January", "February", "March","April","May"]
    # expense_amount = int(input("Enter the expense amount: "))
    # for i,e in enumerate(expense_list):
    #     if e == expense_amount:
    #         if i == 0:
    #             print(f'You spent {e} in {month_list[i]}')
    #             break
    #         elif i==1:
    #             print(f'You spent {e} in {month_list[i]}')
    #             break
    #         elif i ==2:
    #             print(f'You spent {e} in {month_list[i]}')
    #             break
    #         elif i==3:
    #             print(f'You spent {e} in {month_list[i]}')
    #             break
    #         elif i== 4:
    #             print(f'You spent {e} in {month_list[i]}')
    #             break
    #     else:
    #         print(f'You didn\'t spend {expense_amount} in any month')
    # #         break

    # OR

    # if expense_amount in expense_list:
    #     index = expense_list.index(expense_amount)
    #     print(f"You spent {expense_amount} in {month_list[index]}")
    # else:
    #     print(f'You didn\'t spend {expense_amount} in any month')

    # for i in range(5):
    #     tired = input(f"Are you tired? {i+1}km completed (y/n)").lower()
    #     if tired == "y":
    #         print("You did't finish the race!!!")
    #         break
    #     elif tired == "n":
    #         continue
    #     else:
    #         print("Invalid entry. Enter only y/n")
    # else:
    #     finished_race= True

    # if finished_race:
    #     print("You finished the race!!!")

    # s = ""
    # for i in range(5):
    #     s += "*"
    #     print(s)

    # for i in range(5):
    #     for j in range(i+1):
    #         print("*",end="")
    #     print("")

    # for i in range(5):
    #     print(i)
    
    # n = int(input("Enter the number of patterns: "))
    # print_pattern(n)




# def print_pattern(n):
#     """Prints star * pattern accoring the number n"""
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end="")
#         print()

class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()

if __name__ == "__main__":
    main()