cars = [
    {"Model": 'Chrysler 300', "color": 'Orange', 'Year': "2008"},
    {"Model": 'Infiniti QX60', "color": 'Green', 'Year': "2001"},
    {"Model": 'Nissan Altima', "color": 'Blue', 'Year': "2023"},
    {"Model": 'Porsche Cayenne', "color": 'Blue', 'Year': "2011"},
    {"Model": 'Hyundai Tucson', "color": 'Purple', 'Year': "2022"},
    {"Model": 'Mazda CX-5', "color": 'Yelow', 'Year': "2018"},
    {"Model": 'Hyundai Elantra', "color": 'White', 'Year': "1991"},
    {"Model": 'Toyota RAV4', "color": 'White', 'Year': "2009"},
    {"Model": 'Alfa Romeo Giulia', "color": 'Green', 'Year': "1992"},
    {"Model": 'Subaru Forester', "color": 'Blue', 'Year': "2020"},
    {"Model": 'Cadillac Escalade', "color": 'Yelow', 'Year': "1993"},
    {"Model": 'Mitsubishi Outlander', "color": 'Purple', 'Year': "2018"},
    {"Model": 'Ford Explorer', "color": 'Purple', 'Year': "1991"},
    {"Model": 'Toyota Camry', "color": 'Orange', 'Year': "2024"},
    {"Model": 'Mercedes-Benz C-Class', "color": 'Black', 'Year': "2006"},
    {"Model": 'Tesla Model 3', "color": 'Black', 'Year': "2016"},
    {"Model": 'BMW X5', "color": 'White', 'Year': "2023"},
    {"Model": 'Mini Cooper', "color": 'White', 'Year': "2008"},
    {"Model": 'Jeep Grand Cherokee', "color": 'Red', 'Year': "2020"},
    {"Model": 'Nissan Altima', "color": 'Сірий', 'Year': "2024"},
    {"Model": 'Acura MDX', "color": 'Black', 'Year': "1997"},
    {"Model": 'Infiniti QX60', "color": 'White', 'Year': "2016"},
    {"Model": 'Honda CR-V', "color": 'White', 'Year': "2001"},
    {"Model": 'GMC Terrain', "color": 'Red', 'Year': "2011"},
    {"Model": 'Volvo XC90', "color": 'Blue', 'Year': "2002"},
    {"Model": 'Subaru Forester', "color": 'White', 'Year': "1990"},
    {"Model": 'Mini Cooper', "color": 'Purple', 'Year': "2017"},
    {"Model": 'Volkswagen Passat', "color": 'Green', 'Year': "2014"},
    {"Model": 'Dodge Charger', "color": 'Blue', 'Year': "2006"},
    {"Model": 'Volkswagen Passat', "color": 'White', 'Year': "1990"},
    {"Model": 'Fiat 500X', "color": 'Black', 'Year': "2022"},
    {"Model": 'BMW X5', "color": 'White', 'Year': "2025"},
    {"Model": 'BMW X5', "color": 'Yelow', 'Year': "2015"},
    {"Model": 'Tesla Model X', "color": 'White', 'Year': "1990"},
    {"Model": 'Buick Enclave', "color": 'Black', 'Year': "1997"},
    {"Model": 'Audi A6', "color": 'Yelow', 'Year': "2022"},
    {"Model": 'Mini Cooper', "color": 'Black', 'Year': "2005"},
    {"Model": 'Ford Mustang', "color": 'Blue', 'Year': "1990"},
    {"Model": 'Hyundai Elantra', "color": 'Purple', 'Year': "2004"},
    {"Model": 'Jeep Grand Cherokee', "color": 'Orange', 'Year': "2024"}
]


filterr = input('Enter filter ')                                    # Строка отвечающаю за выбор фильтра

def func_color_car(arrays,color):                                   # Функция сортировки по цвету
    return [array for array in arrays if array["color"] == color]

def func_correct_year_car(arrays,year):                             #Функция сортировки за годом
    return [array for array in arrays if array["Year"] == year]




sorted_name_car = sorted(cars, key=lambda name_car: name_car["Model"])  #Сортировка всего масива словарей в алфавитном порядку от A до Z


if filterr == "color car":                              # При написания этих слов применяеться фильтр по цвету авто
    sub_question1 = input('Enter ')                     # Строка отвечающая за выбор цвета на твой выбор
    filtered_data = func_color_car(cars, sub_question1)
    for car in filtered_data:
        print(car)


if filterr == "car name":                               # Условие отвечающие за сортировку в алфавитном порядкею(строка 56)
    for car_name in sorted_name_car:                    # Идет цикл каждого елемена в словаре
            print(car_name)

if filterr == "year car":                               # Условие отвечает за конкретный год авто
    cars.sort(key=lambda y: y.get("Year",0), reverse=True)
    for c in cars:
        print(c)

if filterr == "Corect car year":                        # Отвечает за конкретный год авто
    sub_question2 = input("Enter ")
    correct_year_car = func_correct_year_car(cars,sub_question2)
    for car in correct_year_car:
        print(car)

if filterr == "years and up":                           # Условие отвечает за выбор от года до года
    start = input("Enter start year ")                  # от какого года
    end = input("Enter end year ")                      # до кокого года
    filtered_year = sorted([y for y in cars if start <= y["Year"] <= end], key=lambda y: y["Year"], reverse=True)
    for car in filtered_year:
        print(car)





