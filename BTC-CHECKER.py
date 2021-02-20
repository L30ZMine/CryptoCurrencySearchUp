# By L30Z
# Title Bitcoin SearchUp

# \/ here were importing the needed crypto and re (crypto = the currencies and the infomation, re for replacing the crypto string with a nicer version)
import cryptocompare
import re
import string

# Now to the code

moneyinput = input("(DEFAULT EURO) choose from the list. " + "European Euro = 1, British Pounds = 2, United States Dollar = 3, Russian Rubbles = 4, Japanese Yen = 5, show more = 6 : ")
# \/ defining the Default if the user enters 0, anything 18
moneyformat = "EUR"

# The if function for every Currency
if moneyinput == "1":
    moneyformat = "EUR" #Euro
elif moneyinput == "2":
    moneyformat = "GBP" #British Pounds
elif moneyinput == "3":
    moneyformat = "USD" #United States Dollar
elif moneyinput == "4":
    moneyformat = "RUB" #Russian Rubles
elif moneyinput == "5":
    moneyformat = "JPY" #Japanese Yen (why is it not YEN but instead JPY WTF)
elif moneyinput == "6":
    moneyinput = input("more : Australian Dollar : 7, Candian Dollar = 8, Swiss Franc = 9, Chinese Renminbi = 10, Hong Kong Dollar = 11, New Zealand Dollar = 12, Swedish Krona = 13, South Korean Won = 14, Singapore Dollar = 15, Norwegian Krone = 16, Indian Rupees = 17, for even more = 18 : ")
# /\ adding more to show how cool i am :) only taking like 69248145 hours to add all those below

# \/ the more curriencies 
if moneyinput == "7":
    moneyformat = "AUD" #Australien Dollar
elif moneyinput == "8":
    moneyformat = "CAD" #Canadien Dollar
elif moneyinput == "9":
    moneyformat = "CHF" #Schweizer Fränsche (Swiss franc)
elif moneyinput == "10":
    moneyformat = "CNY" #Chinese Dollar
elif moneyinput == "11":
    moneyformat = "HKD" #Honk Kong Dollar (the situation still fucked tho)
elif moneyinput == "12":
    moneyformat = "NZD" #New Zealand Dollar (I want to visit new zealand sometime, the better australia)
elif moneyinput == "13":
    moneyformat = "SEK" #Swedish Krona (I went there long story short i dint shit for 12 days)
elif moneyinput == "14":
    moneyformat = "KRW" #South Korean Dollar (they're is a dude on tiktok who screams mama in every video hes korean, funny)
elif moneyinput == "15":
    moneyformat = "SGD" #Singapure Dollar
elif moneyinput == "16":
    moneyformat = "NOK" #Norgwegian Krone (seems like a boring country tbh)
elif moneyinput == "17":
    moneyformat = "INR" #Indian Rupees (your computer has virus xD)
elif moneyinput == "18":
    print("FUCK YOU WHERE DO YOU LIVE????, WRITE ME YOUR CURRENCY ILL ADD IT L30Zboss@gmail.com BRUH")
elif moneyinput == "0":
    print("dont type 0 wtf your wierd, REVERTING TO DEFAULT = EUR")

# cryptocompare.get_price(['BTC', 'ETH', 'BCH'], [moneyformat])

cryptoinput = input("(DEFUALT BITCOIN) (FOR MORE THAN 1 USE (bitcoin, etherium, bitcoincash)) Now Select the crypto type: bitcoin, etherium, bitcoincash : ")
cryptoformat = ['BTC', 'ETH', 'BCH']

# with bitcoin first
if cryptoinput == "bitcoin":
    cryptoformat = ['BTC']
elif cryptoinput == "bitcoin, etherium":
    cryptoformat = ['BTC', 'ETH']
elif cryptoinput == "bitcoin, bitcoincash":
    cryptoformat = ['BTC', 'BCH']
elif cryptoinput == "bitcoin, etherium, bitcoincash":
    cryptoformat = ['BTC', 'ETH', 'BCH']
elif cryptoinput == "bitcoin, bitcoincash, etherium":
    cryptoformat = ['BTC', 'BCH', 'ETH']
# now with etherium at first
elif cryptoinput == "etherium":
    cryptoformat = ['ETH']
elif cryptoinput == "etherium, bitcoin":
    cryptoformat = ['ETH', 'BTC']
elif cryptoinput == "etherium, bitcoincash":
    cryptoformat = ['ETH', 'BCH']
elif cryptoinput == "bitcoin, etherium, bitcoincash":
    cryptoformat = ['ETH', 'ETH', 'BCH']
elif cryptoinput == "bitcoin, etherium, bitcoincash":
    cryptoformat = ['ETH', 'BCH', 'BTC']
# lastely with bitcoincash at first
elif cryptoinput == "bitcoincash":
    cryptoformat = ['BCH']
elif cryptoinput == "bitcoincash, etherium":
    cryptoformat = ['BCH', 'ETH']
elif cryptoinput == "bitcoincash, bitcoin":
    cryptoformat = ['BCH', 'BTC']
elif cryptoinput == "bitcoincash, etherium, bitcoin":
    cryptoformat = ['BCH', 'ETH', 'BTC']
elif cryptoinput == "bitcoincash, bitcoin, etherium":
    cryptoformat = ['BCH', 'BTC', 'ETH']

# And after all those if statements the end result :)
print(cryptocompare.get_price(cryptoformat, [moneyformat]))
