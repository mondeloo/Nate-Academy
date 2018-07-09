import datetime
year = int(input("Dime el año: "))
month = int(input("Dime el mes: "))
day = int(input("Dime el dia: "))

user_date = datetime.datetime(year = year, month = month, day = day)

today = datetime.datetime.now()
time_remainig = user_date - today

print("Faltan {} dias y horas {}".format(time_remainig.days, int(time_remainig.seconds / 3600)))

