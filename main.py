import csv
from utils.utils import send_email

server = "smtp.gmail.com"
company = "ACompany" # example
company_email = "xxx@xxxxx.com" # insert the sender's email
password = "********" # insert the sender's password

with open("email_addresses.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for name, email in reader:
        send_email(company, company_email, name, email, password, server)
