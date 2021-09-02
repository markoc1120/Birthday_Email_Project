# Extra Hard Starting Project #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
import random
import os

MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

data = pd.read_csv('birthdays.csv').to_dict(orient='records')
now = dt.datetime.now()
current_date = (now.month, now.day)

for item in data:
    birthday_date = (item['month'], item['day'])

    if current_date == birthday_date:
        random_txt = random.choice(os.listdir('./letter_templates'))

        with open(f'./letter_templates/{random_txt}') as txt:
            random_letter = txt.read().replace('[NAME]', item['name'])

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=item['email'],
                                msg=f"Subject:Happy Birthday!\n\n{random_letter}")
