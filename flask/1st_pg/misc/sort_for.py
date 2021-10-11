def sagasu(city):
    cities = session.query().filter(Test.city==city).all()

    print(cities.city,cities.temp_hi)