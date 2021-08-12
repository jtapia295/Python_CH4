# Assign values to the 6 starting variables:
date = 'Monday 2021-08-11'
time = '03:22:00 PM'
average_astronaut_mass_kg = 80.7
fuel_mass_kg = 760000
ship_mass_kg = 74842.31
fuel_level = '100%'

# Prompt the user for the number of astronauts and the crew status:
crew_size = int(input())
crew_status = input()

# Code your mass calculations here:
crew_total_mass = crew_size * average_astronaut_mass_kg
mass_of_ship = crew_total_mass + ship_mass_kg + fuel_mass_kg

# Display the checklist:
line_sep = ('-------------------')
print(line_sep, '''\n''', '> Launch Checklist', '''\n''',line_sep)
print('Date: ', date)
print('Time: ', time)
'''\n'''
print(line_sep, '''\n''', '> SHIP INFO', '''\n''',line_sep)
print('* Crew: ', str(crew_size))
print('* Crew Status: ',crew_status)
print('* Fuel Level: ',fuel_level)
'''\n'''
print(line_sep, '''\n''', '> MASS DATA', '''\n''',line_sep)
print('* Crew: ',str(crew_total_mass))
print('* Fuel: ',str(fuel_mass_kg))
print('* Spaceship: ',str(ship_mass_kg))
print('* Total Mass: ',str(mass_of_ship))
