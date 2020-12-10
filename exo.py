#1
cities = ['Paris', 'Lyon', 'Marseille', 'Lille', 'Toulouse', 'Bordeaux']
# print(cities)


# #2
# print(cities[0], cities[1], cities[4])


# #3
# sorted_cities = sorted(cities)
# for city in sorted_cities:
#     print(city)


# #4
# cities[1] = 'Strasbourg'
# cities[4] = 'Nice'
# print(cities)


# #5
# cities.append('Rouen')
# cities.append('Reims')
# print(cities)


# # 6
# cities.insert(1, 'Nice')
# cities.insert(3, 'Nantes')
# print(cities)


# #7
# cities.pop(2)
# cities.pop(-1)
# print(cities)


# #8
# cities_2 = ['Strasbourg', 'Nice', 'Rouen']
# cities_3 = ['Tours']

# all_star = cities + cities_2 + cities_3
# print(all_star)

# #9
# print(len(cities))


# #10
# print(sorted(cities))


# #11
# print(sorted(cities, reverse=True))


# #12
# get_first_city = lambda cities : sorted(cities)[0]
# get_last_city = lambda cities : sorted(cities, reverse=True)[0]
# print(get_first_city(cities))
# print(get_last_city(cities))


# #13
# get_first_and_last_land = lambda cities : [sorted(cities)[0], sorted(cities)[-1]]
# print(get_first_and_last_land(cities))


# # 14
# for city in cities:
#     print(city)


# #15
# for city in sorted(cities, reverse=True):
#     print(city)


# #16
# for city in range(len(cities)):
#     if city % 2 == 1:
#         print(cities[city])


# # 17
# for city in cities:
#     city = city + ' (France)'
#     print(city)


# #18
# for city in cities:
#     print(cities)


# #19
# index = 0
# while index < len(cities):
#     print(cities[index])
#     index += 1


# #20
# index = 0
# while index < len(cities):
#     print(sorted(cities, reverse=True)[index])
#     index += 1

# #21
# index = 0
# to_be_removed = []
# while index < len(cities):
#     if len(cities[index]) > 6:
#         to_be_removed.append(cities[index])
        
#     index += 1

# for city in to_be_removed:
#     cities.remove(city)

# ## Better way:
# cities = [city for city in cities if len(city) < 6]
# print(cities)