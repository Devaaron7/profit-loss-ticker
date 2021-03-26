# profit-loss-ticker

Quick Script that will show your current profit / loss value while invested in a listed Crypto currency.

Price is updated every couple seconds

The coin price is pulling from Robinhood's website.

I programmed this as a way to quickly glance and see how an investment is doing without pulling out my phone.

Requires the following Modules - 

bs4
guizero
lxml
requests

optional - I've included a pipfile.lock where you can use pipenv sync to install all needed modules at once

Usage -
1. Install the needed Modules
2. Run Main.py
3. Select your coin using the instructions, enter the amount you invested, and the price of the coin when you invested - then hit enter
4. The screen will fill and display the current profit / loss based on the current price of the coin. You can exit Fullscreen by hitting the "Esc" Key


Example 1 - 
User Invested $1000 into LTC when it was at $177

Litcoin price at 5:39PM on 3/26/21 was around $182.84

![image](https://user-images.githubusercontent.com/65022882/112695876-32c6f580-8e5b-11eb-8dfb-b20848c17176.png)
![image](https://user-images.githubusercontent.com/65022882/112695886-35c1e600-8e5b-11eb-8813-cf4187b0b153.png)

Example 2 - 
User Invested $1000 into BTC when it was at $60,000

Bitcoin price at 5:51PM on 3/26/21 was around $54,620

![image](https://user-images.githubusercontent.com/65022882/112696279-e7f9ad80-8e5b-11eb-9232-37c66208b1ff.png)
![image](https://user-images.githubusercontent.com/65022882/112696284-e9c37100-8e5b-11eb-9799-a82eb29185d5.png)

Thank you for checking this out

- Aaron T
