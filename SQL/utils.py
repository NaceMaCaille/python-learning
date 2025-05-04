import sqlite3
from cars_data import models, colors, years, model_prices, year_prices

def init_db():
    connection = sqlite3.connect('SQL/cars.db')
    cur = connection.cursor()
    cur.executescript("""
            CREATE TABLE IF NOT EXISTS cars(
            model TEXT,
            color TEXT,
            year_of_issue INTEGER,    
            price INTEGER
        )
        """)
    
def get_cars():
    connection = sqlite3.connect('SQL/cars.db')
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

def save_to_db(object):
    model,color,year,price = object
    connection = sqlite3.connect('SQL/cars.db')
    cur = connection.cursor()
    cur.execute("INSERT INTO cars(model, color, year_of_issue,price) VALUES(?,?,?,?)", (model,color,year,price))
    connection.commit()
    cur.close()

def interface_model():

    [print(num + ' -',model) for num,model in models.items()]
    model = input('Оберіть модель авто - ')
    
    [print(num + ' -',color) for num,color in colors.items()]

    color = input('Оберіть колір авто - ')
   
    [print(num + ' -',year) for num,year in years.items()]

    year = input('Оберіть рік виробництва авто - ')
    select_model_car(model,color,year)

def choice_custom_car():
    custom = {
        '1': interface_model,
        '2': get_cars,
        '0': exit
    }

    while True:
        print('1 - Оберіть модель') 
        print('2 - вивести всі авто з бази')
        print('0 - Вихід')

        select = input('Оберіть опцію - ')
        option = custom.get(select)

        if option:
            option()

def select_model_car(select_model,select_color,select_year):
    car_object = []
    s_model = models.get(select_model)
    car_object.append(s_model)

    s_color = colors.get(select_color)
    car_object.append(s_color)
   
    s_year = years.get(select_year)
    car_object.append(s_year)

    price_model = model_prices.get(s_model)
    price_year = year_prices.get(s_year)

    price = str(int(price_model) + int(price_year))
    car_object.append(price)    

    save_to_db(car_object)