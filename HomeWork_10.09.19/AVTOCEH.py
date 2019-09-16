
import random

class Customer():
    def __init__(self, name, address, phoneNumber, money, car):
        self.__name = name
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__money = money
        self.__car = car
    def get_car(self):
        return self.__car
    def get_money(self):
        return self.__money
    def get_phoneNumber(self):
        return self.__phoneNumber
    def get_address(self):
        return self.__address
    def get_name(self):
        return self.__name
    def pay_money(self, target, money):
        self.__money -= money
        target.add_money(money)

    
class Car():    
    def __init__(self, brandDict, modelDict, breakageDict, year = None):       
        self.__brand = list(brandDict.keys())[random.randint(0,len(brandDict)-1)] 
        self.__model = list(modelDict.keys())[random.randint(0,len(modelDict)-1)]
        if year == None:
            self.__year = 2019 - random.randint(0,40)
        self.__breakage = list(breakageDict.keys())[random.randint(0,len(breakageDict)-1)]
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
    def get_breakage(self):
        return self.__breakage

class Company():
    
    def __init__(self, money, brandDict, modelDict, breakageDict):
        self.__money = money
        self.__brandDict = brandDict
        self.__modelDict = modelDict
        self.__breakageDict = breakageDict
        self.dataBase = [("Number", "Name", "Address", "Phone number", "Car data")]

    def add_money(self, money):
        self.__money += money
        
        
    def take_car(self, client):
        car = client.get_car()
        cost = self.__brandDict[car.get_brand] * self.__modelDict[car.get_model] * self.__breakageDict[car.get_breakage]
        print("Здравствуйте,{0}, у вашего автомобиля сломалось {1}, стоимость починки равна {2} рублей, желаете ли вы воспользоваться нашими услугами?('Да','Нет')".format(client.get_name,car.get_breakage,cost)) 
        answer = input()
        if answer == 'Да':
            if client.get_money > cost:
                self.dataBase.append([len(dataBase),client.get_name, client.get_address, client.get_phoneNumber,car])
                client.pay_money(self)
                print("Спасибо, что пользуйтесь услугами Ультрагайки. До свидания")
                return 1
            else:
                print("У вас не хватает денег. До свидания.")
                return 0
        elif answer == 'Нет':
            print("Ну и ладно, не очень то и хотелось")
        
        
        
    
brandDict = {'Mercedes': 2,'Porsche' : 3,'BMW': 1.99}
modelDict = {"Седан" : 1, "Универсал" : 1.1, "Микроавтобус" : 1.5, "Минивэн" : 1.3, "Лимузин" : 1.9}  
breakageDict= { "Ходовая часть" : 15000, "Развал схождения" : 2000,
               "Рулевого управление" : 10000, "Электрика" : 10000,
               "Двигатель" : 20000, "Тормозные системы" : 6000, "Замена жидкостей и фильтров" : 2000,
               "Стёкла" : 7000, "Система впрыска и зажигания" : 4000, "Выхлопная система" : 2000}
car = Car(brandDict, modelDict, breakageDict)
client = Customer("Петров Пётр Петрович", "г. Саратов, Провиантская ул., д. 11, кв. 45", "+71000000000",
                 80000, car)
comp = Company(10000, brandDict, modelDict, breakageDict)
comp.take_car(client)
print(comp.money)
