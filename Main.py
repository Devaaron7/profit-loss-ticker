from guizero import App, Text, PushButton
import random
import time
from guizero import App, Text, PushButton
import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
import requests
import webbrowser
import os
from urllib.error import HTTPError

def show():
        try:
                req = Request(URL[user_choice])
                webpage = urlopen(req).read()
                soup = bs.BeautifulSoup(webpage, "xml")
                remove = ["$", ",", "."]
                current =""

                # For loop that loops through all the span classes that display the price of Ether, then adds them to a list
                for x in soup.find_all(class_="T_ocKK8QpgJxwxluz95GC up css-1baulvz"):
                    for z in x:
                        if z not in remove:
                            current += z

                if user_choice == 1:
                    num = float(current) *.000001
                else:
                    num = float(current) *.01

                #print("Currect Price: $ {}".format(num))


                increase = num
                #print("asset current price: $", increase)
                
                p = percentage(increase, asset)

                #print("Investment increase / decreased % by: ", p * 100, "%")
                
                i = (o_i + (o_i * p))

                s = i - o_i
                #s = 10
                if s > 0:
                        text.text_color = "green"
                        text.value = "+", round(s, 2)
                else:
                        text.text_color = "red"
                        text.value = round(s, 2)
                text.after(1000, show)
        except HTTPError as err:
                if err == 504:
                        pass
        

    

def percentage(inc, org):
    #print(inc, org)
    n = inc - org
    #print(n)
    return n / org

print("""
0. Ethereum
1. Dogecoin
2. Bitcoin
3. Bitcoin Cash
4. Litecoin
5. Roblox
6. Coinbase
""")

URL = ["https://robinhood.com/crypto/ETH", "https://robinhood.com/crypto/DOGE", "https://robinhood.com/crypto/btc", "https://robinhood.com/crypto/BCH", "https://robinhood.com/crypto/ltc", "https://robinhood.com/stocks/RBLX", "https://robinhood.com/stocks/COIN"]

coin_name = ["Ethereum", "Dogecoin", "Bitcoin", "Bitcoin Cash", "Litecoin", "Roblox", "Coinbase"]

error = list(range(0, len(URL)))

user_choice = int(input("Please enter the number of a item from the list to track\n"))

while user_choice not in error:
    user_choice = int(input("Invalid choice. Please enter the number of a item from the list to track\n"))
print("User chose to track ", coin_name[user_choice], "\n")


o_i = float(input("Enter Investment\n"))

i = 0

i += o_i

asset = float(input("Enter asset price at time of investment\n"))






'''
while True:
        req = Request(URL[user_choice])
        webpage = urlopen(req).read()
        soup = bs.BeautifulSoup(webpage, "xml")
        remove = ["$", ",", "."]
        current =""

        # For loop that loops through all the span classes that display the price of Ether, then adds them to a list
        for x in soup.find_all(class_="T_ocKK8QpgJxwxluz95GC up css-1baulvz"):
            for z in x:
                if z not in remove:
                    current += z

        if user_choice == 1:
            num = float(current) *.000001
        else:
            num = float(current) *.01

        #print("Currect Price: $ {}".format(num))


        increase = num
        #print("asset current price: $", increase)
        
        p = percentage(increase, asset)

        #print("Investment increase / decreased % by: ", p * 100, "%")
        
        i = (o_i + (o_i * p))

        s = i - o_i

        #print("$", s)
'''

app = App()
text = Text(app, size = 250, color="blue")
#text.repeat(1000, show)
text.after(1000, show)
app.display()
