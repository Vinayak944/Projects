def main():
    file_path = r'C:\Users\Vinayak Ganesh\Projects\PythonProjects\exersises\stocks_programs\stocks.csv'
    calculate_ratio(file_path)

# def calculate_ratio(file_path):
#     """Calculate the pe ratio and price to book ratio from the stocks.csv data"""

#     with open(file_path,'r') as file:
        
#         output_data = []
#         """ READ THE FILE LINE BY LINE use this method before the read()
#         or any other method that moves through the file since the cursor have been moved
#         """
#         # for line in file:
#             # print(type(line))
        
#         ''' readline() reads just the first line or the first'\n' and 
#             READLINES() reads the file line by line and stores it as a list'''
#         title = file.readline().rstrip()
#         output_data.append(title)
#         content = file.readlines()

#         # company_name = []
#         # price = []
#         # earnings_per_share = []
#         # book_value = []

#         for l in content:
#             data = l.rstrip().split(",")
#             company_name, price, earnings_per_share, book_value = data
#             # print(company_name,price,earnings_per_share,book_value)
#             price = float(price)
#             earnings_per_share = float(earnings_per_share)
#             book_value = float(book_value)
#             pe_ratio = price / earnings_per_share
#             price_to_book_ratio = price / book_value
#             # print(round(pe_ratio,2),round(price_to_book_ratio,2))
#             output_line = f"{company_name},{pe_ratio:.2f},{price_to_book_ratio:.2f}"
#             output_data.append(output_line)
#         # print('\n'.join(output_data))
#     with open('Output.csv','w') as output_file:
#         output_file.write('\n'.join(output_data))
#         # for t in title:
#              # print(t)
#         # print(content)

def calculate_ratio(file_path):

    output_path = r'C:\Users\Vinayak Ganesh\Projects\PythonProjects\exersises\stocks_programs\stocks_draft_Output2.csv'

    with open(file_path,'r') as file, open(output_path,'w') as output_file:
        output_file.write('Company Name,PE ratio, PB ratio\n')
        next(file)

        for line in file:
            data = line.strip().split(',')

            try:
                company_name = data[0]
                price = float(data[1])
                earnings_per_share = float(data[2])
                book_value = float(data[3])
                pe_ratio = price / earnings_per_share
                price_to_book_ratio = price / book_value
                output_file.write(f'{company_name},{pe_ratio:.2f},{price_to_book_ratio:.2f}\n')
            except ValueError:
                pass

if __name__ == "__main__":
    main()