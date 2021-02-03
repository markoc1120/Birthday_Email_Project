# ---------------------- Extra Hard Starting Project ---------------------- #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the
# [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import json
import smtplib
import os
import random

my_email = "testingmarkpython@gmail.com"
password = "Bc##9f60Zm4ipd"
now = dt.datetime.now()

path, dirs, files = next(os.walk("./letter_templates"))
file_count = len(files)

birthdays = pandas.read_csv("birthdays.csv")
pandas.DataFrame(birthdays).to_json("birthdays.json", orient="records")
with open("birthdays.json") as file:
    birthdays_json = json.load(file)

with open(f"./letter_templates/letter_{random.randint(1, file_count)}.txt") as letter:
    email_list = letter.readlines()

for item in birthdays_json:
    if now.month == item["month"] and now.day == item["day"]:
        email_string = "".join(email_list).replace("[NAME]", f"{item['name']}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="h.markoc1120@gmail.com", msg="Subject:Happy Birthday!"
                                                                                           f"\n\n{email_string}")
