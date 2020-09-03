from bs4 import BeautifulSoup
import requests
import os, os.path, csv

#test

url = 'https://www.tgju.org/gold-chart'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#chon felan farsi parse nemikone script python , index list prices:
#1.bours
#2.ons tala
#3.mesghal tala
#4.tala 18
#5.seke
#6.dollar
#7.euro
#8.naft berent
#9.bitcoin
prices=[]

data = soup.findAll('span', {"class":"info-price"})
for d in data:
	prices.append(d.get_text())



print(prices)
print('Test has been completed')
