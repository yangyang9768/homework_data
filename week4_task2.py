"""
Using exception handling code blocks such as try/ except / else / finally, write a program that simulates an ATM machine to withdraw money.
(NB: the more code blocks the better, but try to use at least two key words e.g. try/except)
Tasks:
1.       Prompt user for a pin code
2.       If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit        a  program.
3.       Set account balance to 100.
4.       Now we need to simulate cash withdrawal
5.       Accept the withdrawal amount
6.       Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
7.       However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program.
"""

# constants
CORRECT_PIN_CODE = 9987

# state of the system
logged_in = False
account_balance = 100


def prompt_number(request, error):
    value = input(request)
    try:
        return int(value)
    except ValueError:
        raise ValueError(error)


def validate_password(correct_password):
    input_password = prompt_number(
        'Enter your PIN: ', error="Please enter a PIN number, ony digits are allowed")

    if input_password != correct_password:
        raise ValueError("You entered the wrong password, please try again")
    # PIN matches
    return True


def login(correct_password):
    global logged_in

    pswEnter_time = 0
    while pswEnter_time < 3:
        print(pswEnter_time)
        try:
            validate_password(correct_password)
        except ValueError as exc:
            print(exc)
            pswEnter_time += 1
        else:
            logged_in = True
            print("you have Login, please operate your account")
            break
    else:
        raise AssertionError(
            'you have reach maxium amount of enter times, please wait 24 hour')


def withdraw_validation(account_balance, transaction_amount):
    if account_balance-transaction_amount < 0:
        raise ValueError('your amount is not enough,exit')


def withdraw_cash(account_balance):
    try:
        transaction_amount = int(
            input('How many money do you want to withdraw'))
        withdraw_validation(account_balance, transaction_amount)
    except ValueError as exp:
        print(exp)
    else:
        account_balance = account_balance-transaction_amount
        print(
            f'you have deduct {transaction_amount} from your account, the total amount in your account is {account_balance} now')
    finally:
        return account_balance
        print(account_balance)


def main():
    '''
    Login a user, then perform a withdraw of money
    '''
    login(CORRECT_PIN_CODE)
    withdraw_cash(account_balance)


if __name__ == "__main__":
    main()
