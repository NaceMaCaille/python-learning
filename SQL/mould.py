models = {'1':'Toyota','2':'BMW','3':'Mercedes-Benz','4':'Tesla','5':'Volkswagen','6':'Honda','7':'Ford','8':'Hyundai','9':'Audi','10':'Kia'}
colors = {'1':'Білий','2':'Чорний','3':'Червоний','4':'Блакитний','5':'Сірий'}
years = {'1':'2019','2':'2020','3':'2021','4':'2022','5':'2023'}
model_prices = {'BMW':'45000','Mercedes-Benz':'48000','Audi':'45000','Volkswagen':'28000','Ford':'26000','Hyundai':'22000','Kia':'22000','Toyota':'23000','Honda':'24000','Tesla':'39000'}
year_prices = {'2019':'1000','2020':'1100','2021':'1200','2022':'1300','2023':'1400'}

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

    