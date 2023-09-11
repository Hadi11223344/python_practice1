first_name = input('Enter Your first name: ')
last_name = input('Enter Your last name: ')
print('Enter Your date of birth: ')
month = input('month? ')
day = input( 'day? ')
year = input('year? ')

print(first_name, last_name,'was born on' , month, day, year)
# the other way to print is
print(f'{first_name} {last_name} was born on {month}, {day} {year}.' )
