# Question 1
# Create a program that tells you whether or not you need an umbrella when you leave
# the house.
# The program should:
# 1. Ask you if it is raining using input()
# 2. If the input is 'y', it should output 'Take an umbrella'
# 3. If the input is 'n', it should output 'You don't need an umbrella'

from datetime import timetuple
import imp


weather = input('if it is raining?')

if weather == 'y':
    print('Take an umbrella')
if weather == 'n':
    print("You don't need an umbrella")


# Question 2
# I'm on holiday and want to hire a boat. The boat hire costs £20 + a refundable £5
# deposit. I've written a program to check that I can afford the cost, but something
# doesn't seem right. Have a look at my program and work out what I've done wrong


# Answer: the input is string

my_money = int(input('How much money do you have? '))

boat_cost = 20 + 5
if my_money < boat_cost:
    print('You cannot afford the board hire')
else:
    print('You can afford the boat hire')


#  Question 3
#       Your friend works for an antique book shop that sells books between 1800 and 1950
#       and wants to quickly categorise books by the century and decade that they were
#       written. Write a program that takes a year(e.g. 1872) and outputs the century and
#       decade(e.g. "Eighteenth Century, Seventies")

book_year = int(input('which year it is?'))


def year_to_century_name(year):
    century = int(year/100)
    if century == 18:
        century_time = 'Eighteenth'
    else:
        century_time = 'nineteenth'
    return century_time


def get_decade(year):
    decade = int((year % 100)/10)
    if decade == 9:
        decade_time = 'Nineties'
    if decade == 8:
        decade_time = 'Eighties'
    if decade == 7:
        decade_time = 'Seventies'
    if decade == 6:
        decade_time = 'Sixties'
    if decade == 5:
        decade_time = 'Fifties'
    if decade == 4:
        decade_time = 'Fourties'
    if decade == 3:
        decade_time = 'Thirties'
    if decade == 2:
        decade_time = 'Twenties'
    if decade == 1:
        decade_time = 'Tens'
    if decade == 0:
        decade_time = 'Hunderds'
    return decade_time


print(f'{year_to_century_name(book_year)}Century,{get_decade(book_year)}')
