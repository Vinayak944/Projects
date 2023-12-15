import requests 
from bs4 import BeautifulSoup
# import matplotlib.pyplot as plt

def main():
    url = "https://in.bookmyshow.com/explore/movies-alappuzha"
    r = requests.get(url, timeout=10)
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    print(soup.find_all('a'))

if __name__ == "__main__":
    main()