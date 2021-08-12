#Chp4-Excersise PartB
    #Variables
name_of_spaceship = 'Determination'
ship_speed_mph = 17500
distance_to_mars_km = 225000000
miles_per_km = 0.621
distance_to_moon_km = 384400

#Calculations
miles_to_mars = distance_to_mars_km * miles_per_km
hours_to_mars = miles_to_mars / ship_speed_mph
days_to_mars = hours_to_mars // 24
days_to_moon = "{:.2f}".format(days_to_target_calulator(ship_speed_mph,distance_to_moon_km))


def days_to_target_calulator(speed_mph, distance_km):
    miles_to_target = distance_km * 0.621
    hours_to_target = miles_to_target / speed_mph
    days_to_target = hours_to_target / 24
    return days_to_target

#Days to Mars
print(name_of_spaceship + ' will take ' + str(days_to_mars) + ' days to reach Mars ')

#Days to Moon
print(name_of_spaceship + ' will take ' + days_to_moon + ' days to reach Moon ')
