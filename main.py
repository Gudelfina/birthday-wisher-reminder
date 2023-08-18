import pandas
import datetime as dt
import random
import smtplib
from personal import my_email, other_email, password


birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row['month'], row['day']): row for (index, row) in birthday_data.iterrows()}


current_date = dt.datetime.now()
current_day_month = (current_date.month, current_date.day)

if current_day_month in birthday_dict:

    file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file) as f:
        letter = f.read()

    birthday_person = birthday_dict[current_day_month]
    birthday_letter = letter.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=other_email,
            msg=f"Subject: Happy Birthday!\n\n {birthday_letter}")
