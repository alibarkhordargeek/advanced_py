import re
import requests
from bs4 import BeautifulSoup
import mysql.connector
carname = input('your favorite car: ')
r = requests.get('https://www.truecar.com/shop/new/?filterType=brand&makeSlug=%s' %carname)
soup = BeautifulSoup(r.text, 'html.parser')
posts = soup.find_all('a', attrs = {'class':'block text-center _7suapx'})
cars = list()
for car in posts:
    car = re.findall(r'(\w+) at (\$\d+\,\d+)', car.text)
    car = car[0]
    cars.append([car[0], car[1]])

cnct = mysql.connector.connect(user='root', password='',
host='127.0.0.1', database='scrape')
cursor = cnct.cursor()
for i in range(0, len(cars)):
    name = cars[i][0]
    price = cars[i][1]
    cursor.execute('insert into truecar values (\'%s\', \'%s\')' %(name, price))
cnct.commit()
cnct.close()