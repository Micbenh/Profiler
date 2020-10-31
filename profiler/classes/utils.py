import random

def password_generator():
    lower_letters = list('qwertyuiopasdfghjklzxcvbnm')
    upper_letters = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    numbers = list('1234567890')
    symbols = list("!@#$%^&*")

    password = ''.join(random.sample(random.choices(lower_letters, k=6) + random.choices(upper_letters, k=6) + random.choices(numbers, k=6) + random.choices(symbols, k=6), 24 ))
    return password

