import random
import string

def password_generator(Len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = "",

    for i in range(0, Len_pass):
        digit = random.choice(options)
        password_user = password_user + digit