from statistics import mean 
stock_price = {
    "info":[600,630,620],
    "ril" :[1430,1490,1567],
    "mtl" :[234,180,160],
}

def add():
    stock = input("Enter the stock to add: ").lower()
    if stock in stock_price:
        print("Stock already exists in the database. Enter the updated price")
        p = [int(input(f"Enter the price of {stock} on day {i + 1}: ")) for i in range(len(stock_price[stock]))]
        stock_price[stock] = p
    else:
        p = [int(input(f"Enter the price of {stock} on day {i + 1}: ")) for i in range(3)]
        stock_price[stock] = p
    print_all()

def print_all():
    for stock,p in stock_price.items():
        avg = mean(stock_price[stock])
        print(f"{stock}==>{p} ==> avg:",round(avg,2))

def main():
    op = input("Enter an operation(add,printall)\n")
    if op.lower() == 'add':
        add()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()