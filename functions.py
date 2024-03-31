from postgres.sql_connect import DATABASE
from collections import namedtuple
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def get_user_data(user_input:str):
    for i in ['username', 'phone_number', 'email']:
        query = f"select * from user_table where {i} = '{user_input}'"
        data = DATABASE.connect(query, 'select')
        if data:
            USER = namedtuple('USER', ['first_name', 'last_name', 'email', 'phone_number', 'username', 'password'])
            current_user = USER(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5] )
            return current_user

    return False
def send_email(user_email: str) -> str:
    sender_email = "qalamochirgich@gmail.com"
    sender_password = "enpdjqayzsxcxqfv"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = 'Instagram Confirmation Code'

    code = str(random.randint(10000,99999))
    message.attach(MIMEText(code, 'plain'))

    with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        text = message.as_string()
        connection.sendmail(sender_email, user_email, msg= text)

    return code
def return_email():
    email = input('Email: ')
    if get_user_data(email) == False:
        if verify_email(email) == True:
            return email
    else:
        print('User With This Email Already Registered! ')
        return return_email()
def return_phone_number():
    phone_number = input('Phone Number: ')
    if get_user_data(phone_number) == False:
        return phone_number
    else:
        print('User With This Phone Number Already Registered! ')
        return return_phone_number()
def return_username():
    username = input('Username: ')
    if get_user_data(username) == False:
        return username
    else:
        print('This Username is Already Taken! ')
        return return_username()
def return_password():
    password = input('Password: ')
    upper = 0
    lower = 0
    symbol = 0
    number = 0
    if len(password) < 8:
        print('Minimum Password Lengths Is 8')
        return return_password()
    else:
        for i in password:
            if i.isdigit():
                number += 1
            elif i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            else:
                symbol += 1

        if number >= 1 and upper >= 1 and lower >= 1 and symbol >= 1:
            return password
        else:
            print("The password must contain at least one Number, one Lowercase, one Uppercase letter, and one Symbol")
            return return_password()
def verify_email(email):
    sent_code = send_email(email)
    for i in range (3):
        vercode = input('Enter The Verification Code: ')
        if vercode == sent_code:
            return True

    while True:
        choice = input("""
    1. Go Back
    2. Resend a New Code
    """)

        if choice == '1':
            return False
        elif choice == '2':
            return verify_email(email)
def register():
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    email = return_email()
    phone_number = return_phone_number()
    username = return_username()
    password = return_password()

    USER = namedtuple('USER', ['first_name', 'last_name', 'email', 'phone_number', 'username', 'password'])
    current_user = USER(first_name, last_name, email, phone_number, username, password)
    print(add_user(current_user))
def add_user(current_user):
    query = f"insert into user_table (first_name, last_name, email, phone_number, username, password) values ('{current_user.first_name}', '{current_user.last_name}', '{current_user.email}', '{current_user.phone_number}','{current_user.username}', '{current_user.password}')"
    DATABASE.connect(query, 'insert')
    return 'Congrats Successfully Registered!!!'

def login():
    user_input = input('0. Go Back \nEmail or Phone number or Username: ')
    if user_input == '0':
        return
    else:
        cur_user = get_user_data(user_input)
        if cur_user == False:
            print('User With This Detail Is Not Available')
            return login()
        else:

            for i in range(3):
                password = input('Enter the password: ')
                if password == cur_user.password:
                    return 'Logged in Successfully'
                else:
                    print('Wrong Password')
            else:
                return 'Could Not Log In'

