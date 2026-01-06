cities_input = input("Введите 5 городов через запятую: ")
cities = cities_input.split(',')
len_ = len(cities)

for i in range(len_):
    city_name = cities[i]
    print(f"Город {i + 1}: {city_name}")
    if 'a' in city_name.lower():
        print(f"(в этом городе есть 'a')")
