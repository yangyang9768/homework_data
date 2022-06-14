# I have a list of things I need to buy from my supermarket of choice. I want to know what the first thing I need to buy is . However, when I run the program it shows me a different answer to what I was expecting? What is the mistake? How do I fix it.

# Answer: the first thing in the List should be Zero
import random
shopping_list = [
    "oranges",
    "cat food",
    "sponge cake",
    "long-grain rice",
    "cheese board",
]
print(shopping_list[0])


# Question 2
# I'm setting up my own market stall to sell chocolates. I need a basic till to check the prices of different chocolates that I sell. I've started the program and included the chocolates and their prices. Finish the program by asking the user to input an item and then output its price.

chocolates = {

    'white': 1.50,

    'milk': 1.20,

    'dark': 1.80,

    'vegan': 2.00,

}

select = input('what do you want')
print(f'the price of {select} chocolate is {chocolates[select]}')


# Question 3
# Write a program that simulates a lottery. The program should have a list of seven numbers that represent a lottery ticket. It should then generate seven random numbers. After comparing the two sets of numbers, the program should output a prize based on the number of matches:
# ·         £20 for three matching numbers
# ·         £40 for four matching numbers
# ·         £100 for five matching numbers
# ·         £10000 for six matching numbers
# ·         £1000000 for seven matching numbers

win_number = [1, 13, 35, 57, 89, 80]
system_gennerate_number = [random.randint(1, 100) for i in range(1, 7)]


def check_price(win_number, generate_numbers):
    print(generate_numbers)
    match_times = 0
    for number in generate_numbers:
        if win_number.count(number) >= 1:
            match_times = match_times+1
    print(match_times)
    return match_times


def give_price(num):
    if num == 3:
        print('you win £20')
    if num == 4:
        print(' you win £40')
    if num == 5:
        print('you win £100')
    if num == 6:
        print('you win £10000')
    if num == 7:
        print('you win £100000')
    else:
        print('you lose')


match_num = check_price(win_number, system_gennerate_number)

give_price(match_num)
