cars = [
    {"Model": 'Chrysler 300', "Color": 'Orange', 'Year': "2008"},
    {"Model": 'Infiniti QX60', "Color": 'Green', 'Year': "2001"},
    {"Model": 'Nissan Altima', "Color": 'Blue', 'Year': "2023"},
    {"Model": 'Porsche Cayenne', "Color": 'Blue', 'Year': "2011"},
    {"Model": 'Hyundai Tucson', "Color": 'Purple', 'Year': "2022"},
    {"Model": 'Mazda CX-5', "Color": 'Yelow', 'Year': "2018"},
    {"Model": 'Hyundai Elantra', "Color": 'White', 'Year': "1991"},
    {"Model": 'Toyota RAV4', "Color": 'White', 'Year': "2009"},
    {"Model": 'Alfa Romeo Giulia', "Color": 'Green', 'Year': "1992"},
    {"Model": 'Subaru Forester', "Color": 'Blue', 'Year': "2020"},
    {"Model": 'Cadillac Escalade', "Color": 'Yelow', 'Year': "1993"},
    {"Model": 'Mitsubishi Outlander', "Color": 'Purple', 'Year': "2018"},
    {"Model": 'Ford Explorer', "Color": 'Purple', 'Year': "1991"},
    {"Model": 'Toyota Camry', "Color": 'Orange', 'Year': "2024"},
    {"Model": 'Mercedes-Benz C-Class', "Color": 'Black', 'Year': "2006"},
    {"Model": 'Tesla Model 3', "Color": 'Black', 'Year': "2016"},
    {"Model": 'BMW X5', "Color": 'White', 'Year': "2023"},
    {"Model": 'Mini Cooper', "Color": 'White', 'Year': "2008"},
    {"Model": 'Jeep Grand Cherokee', "Color": 'Red', 'Year': "2020"},
    {"Model": 'Nissan Altima', "Color": 'Сірий', 'Year': "2024"},
    {"Model": 'Acura MDX', "Color": 'Black', 'Year': "1997"},
    {"Model": 'Infiniti QX60', "Color": 'White', 'Year': "2016"},
    {"Model": 'Honda CR-V', "Color": 'White', 'Year': "2001"},
    {"Model": 'GMC Terrain', "Color": 'Red', 'Year': "2011"},
    {"Model": 'Volvo XC90', "Color": 'Blue', 'Year': "2002"},
    {"Model": 'Subaru Forester', "Color": 'White', 'Year': "1990"},
    {"Model": 'Mini Cooper', "Color": 'Purple', 'Year': "2017"},
    {"Model": 'Volkswagen Passat', "Color": 'Green', 'Year': "2014"},
    {"Model": 'Dodge Charger', "Color": 'Blue', 'Year': "2006"},
    {"Model": 'Volkswagen Passat', "Color": 'White', 'Year': "1990"},
    {"Model": 'Fiat 500X', "Color": 'Black', 'Year': "2022"},
    {"Model": 'BMW X5', "Color": 'White', 'Year': "2025"},
    {"Model": 'BMW X5', "Color": 'Yelow', 'Year': "2015"},
    {"Model": 'Tesla Model X', "Color": 'White', 'Year': "1990"},
    {"Model": 'Buick Enclave', "Color": 'Black', 'Year': "1997"},
    {"Model": 'Audi A6', "Color": 'Yelow', 'Year': "2022"},
    {"Model": 'Mini Cooper', "Color": 'Black', 'Year': "2005"},
    {"Model": 'Ford Mustang', "Color": 'Blue', 'Year': "1990"},
    {"Model": 'Hyundai Elantra', "Color": 'Purple', 'Year': "2004"},
    {"Model": 'Jeep Grand Cherokee', "Color": 'Orange', 'Year': "2024"}
]


filterr = input('Enter filter ')                                    

def func_color_car(arrays,color):                                   
    return [array for array in arrays if array["Color"] == color]

def func_correct_year_car(arrays,year):                             
    return [array for array in arrays if array["Year"] == year]

def func_car_name(arrays,name):
    return[array for array in arrays if array["Model"] == name]

def custom_car(arrays=[10],color=[10],year=[10],model=[10]):
    def matches(search,value):
        return search is None or str(search).lower() in str(value).lower()
    return [
        car for car in arrays
        if matches(car.get("Model"), model)
        and matches(car.get("Color"), color)
        and matches(car.get("Year"), year)
    ]


sorted_name_car = sorted(cars, key=lambda name_car: name_car["Model"])  


if filterr == "color car":                              
    sub_question1 = input('Enter ')                     
    filtered_data = func_color_car(cars, sub_question1)
    for car in filtered_data:
        print(car)


if filterr == "car name":
    name_car = input("Enter name car ")
    similar_name = [{key: value for value,key in cars.items() if name_car in key} for item in cars if isinstance(item, dict)]
    func_model = func_car_name(cars,name_car)           
    for car_name in func_model:                    
            print(car_name)

if filterr == "year car":                               
    cars.sort(key=lambda y: y.get("Year",0), reverse=True)
    for c in cars:
        print(c)

if filterr == "Corect car year":                        
    sub_question2 = input("Enter ")
    correct_year_car = func_correct_year_car(cars,sub_question2)
    for car in correct_year_car:
        print(car)

if filterr == "years and up":                           
    start = input("Enter start year ")                  
    end = input("Enter end year ")                      
    filtered_year = sorted([y for y in cars if start <= y["Year"] <= end], key=lambda y: y["Year"], reverse=True)
    for car in filtered_year:
        print(car)

if filterr == "Custom car":
    model = input('Enter model ')
    color = input('Enter color ')
    year = input('Enter year ')
    filtered_car = custom_car(cars,color,year,model)
    for car in filtered_car:
        print(car)






