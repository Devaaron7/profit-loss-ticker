from guizero import App, Text, PushButton
import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
import requests
import webbrowser
import os

def show():

        req = Request(URL[user_choice])
        webpage = urlopen(req).read()
        soup = bs.BeautifulSoup(webpage, "xml")
        remove = ["$", ",", "."]
        current =""

        for x in soup.find_all(class_="T_ocKK8QpgJxwxluz95GC up css-1baulvz"):
            for z in x:
                if z not in remove:
                    current += z

        if user_choice == 1:
            num = float(current) *.000001
        else:
            num = float(current) *.01

        increase = num
        
        p = percentage(increase, asset)
        
        investment = (cash + (cash * p))

        result = investment - cash

        if result > 0:
                text.text_color = "green"
                text.value = "+", round(result, 2)
        else:
                text.text_color = "red"
                text.value = round(result, 2)
        text.after(1000, show)

        

    

def percentage(inc, org):
    n = inc - org
    return n / org



print("""
0. Ethereum
1. Dogecoin
2. Bitcoin
3. Bitcoin Cash
4. Litecoin
""")

URL = ["https://robinhood.com/crypto/ETH", "https://robinhood.com/crypto/DOGE", "https://robinhood.com/crypto/btc", "https://robinhood.com/crypto/BCH", "https://robinhood.com/crypto/ltc", "https://robinhood.com/stocks/RBLX"]
coin_name = ["Ethereum", "Dogecoin", "Bitcoin", "Bitcoin Cash", "Litecoin"]
error = list(range(0, len(URL) - 1))
user_choice = int(input("Please enter the number of a item from the list to track\n"))
while user_choice not in error:
    user_choice = int(input("Invalid choice. Please enter the number of a item from the list to track\n"))
print("User chose to track ", coin_name[user_choice], "\n")

cash = float(input("Enter Investment\n"))

investment = 0

investment += cash

asset = float(input("Enter asset price at time of investment\n"))




app = App()
text = Text(app, size = 250, color="blue", width="fill", height="fill")
text.after(1000, show)
app.set_full_screen()
app.display()
