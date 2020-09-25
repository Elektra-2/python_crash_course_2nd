# City Names: Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    """Return a combined string to show city and country"""
    return f" {city.title()}, {country.title()}"


#  Calling Function
city = city_country('sao paulo', 'brasil')
print(city)

city = city_country('buenos aires', 'argentina')
print(city)

city = city_country('vancouver', 'canada')
print(city)



