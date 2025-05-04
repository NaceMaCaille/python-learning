<<<<<<< Updated upstream
from utils import init_db, choice_custom_car
    
init_db()
=======
import sqlite3
import mould

def init_db():
    connection = sqlite3.connect('cars.db')
    cur = connection.cursor()
    cur.executescript("""
            CREATE TABLE IF NOT EXISTS cars(
            model TEXT,
            color TEXT,
            year_of_issue INTEGER,    
            price INTEGER
        )
        """)
    
init_db()

models = {'1':'Toyota','2':'BMW','3':'Mercedes-Benz','4':'Tesla','5':'Volkswagen','6':'Honda','7':'Ford','8':'Hyundai','9':'Audi','10':'Kia'}
colors = {'1':'Білий','2':'Чорний','3':'Червоний','4':'Блакитний','5':'Сірий'}
years = {'1':'2019','2':'2020','3':'2021','4':'2022','5':'2023'}
model_prices = {'BMW':'45000','Mercedes-Benz':'48000','Audi':'45000','Volkswagen':'28000','Ford':'26000','Hyundai':'22000','Kia':'22000','Toyota':'23000','Honda':'24000','Tesla':'39000'}
year_prices = {'2019':'1000','2020':'1100','2021':'1200','2022':'1300','2023':'1400'}

def get_cars():
    connection = sqlite3.connect('cars.db')
    cur = connection.cursor()

    cur.execute('SELECT * FROM cars;')
    cars = cur.fetchall()
    for car in cars:
        print(car)
    if (len(cars) == 0):
        print()
        print('В таблиці поки немає машин.')
        print()
    connection.close()


def choice_custom_car():
    def interface_model():
        print("""
        1 - Toyota
        2 - BMW
        3 - Mercedes-Benz
        4 - Tesla
        5 - Volkswagen
        6 - Honda
        7 - Ford
        8 - Hyundai
        9 - Audi
        10 - Kia
        """)
        model = input('Оберіть модель авто - ')
        

    
        print("""
        1 - Білий
        2 - Чорний
        3 - Червоний
        4 - Блакитний
        5 - Сірий
        """)

        color = input('Оберіть колір авто - ')
    

   
        print(""" 
        1 - 2019
        2 - 2020
        3 - 2021
        4 - 2022
        5 - 2023
        """)

        year = input('Оберіть рік виробництва авто - ') 
        save_to_db(mould.select_model_car(model,color,year))

    custom = {
        '1':interface_model,
        '2':get_cars,
        '0':exit
    }

    while True:
        print('1 - Оберіть модель') 
        print('2 - вивести всі авто з бази')
        print('0 - Вихід')

        select = input('Оберіть опцію - ')
        option = custom.get(select)

        if option:
            option()
 


def save_to_db(object):
    connection = sqlite3.connect('cars.db')
    cur = connection.cursor()
    model,color,year,price = object
    cur.execute("INSERT INTO cars(model, color, year_of_issue,price) VALUES(?,?,?,?)", (model,color,year,price))
    connection.commit()
    cur.close()

>>>>>>> Stashed changes
choice_custom_car()