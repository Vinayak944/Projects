def main():
    file_path = r'PythonProjects/exersises/stocks_programs/stocks.csv'
    calculate_ratio(file_path)

def calculate_ratio(file_path):
    """Calculate the pe ratio and price to book ratio from the stocks.csv data"""

    with open(file_path,'r') as file:

        output_data = []
        output_path = r'C:\Users\Vinayak Ganesh\Projects\PythonProjects\exersises\stocks_programs\stocks_Output.csv'
        next(file)
        content = file.readlines()

        for l in content:
            data = l.rstrip().split(",")
            company_name, price, earnings_per_share, book_value = data
            price = float(price)
            earnings_per_share = float(earnings_per_share)
            book_value = float(book_value)
            pe_ratio = price / earnings_per_share
            price_to_book_ratio = price / book_value
            output_line = f"{company_name},{pe_ratio:.2f},{price_to_book_ratio:.2f}"
            output_data.append(output_line)

    with open(output_path,'w') as output_file:
        output_file.write('Company Name,PE Ratio,PB Ratio\n')
        output_file.write('\n'.join(output_data))

if __name__ == "__main__":
    main()