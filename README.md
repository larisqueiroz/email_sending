# email_sending
An email sending system with random confirmation code.

## Description
Confirmation emails are sent based on the list of email addresses. Each email's content has a greeting with the receiver's name and a six digit random confirmation code. In case of error, the description along with date and time will be saved on the log file.

## Architecture

    -+- assets                  
     |    |
     |    +- ACompany.png
     |
     +- template                  
     |    |
     |    +- index.html      
     |                          
     +- utils
     |    |
     |    +- utils.py
     |
     - email_addresses.csv                
     |     
     |                          
     - log.txt
     |
     |
     - main.py
     |
     |
     - README.md
     |
     |
     - run.bat

## Built With
* Programming language: Python
* HTTP
* csv
* email.mime
* ssl
* datetime
* smtplib

## Get started
1. Create a new gmail account

This project send emails through Gmail and to do so, the code needs permition. You can do it by editing security settings on your Gmail account. However, it's not cool doing it on your personal account. So, the best choice is to create a new one for this purpose.

Turn this option ON: https://myaccount.google.com/lesssecureapps

2. Insert your email credentials on main.py.

3. Populate the email_addresses.csv file with the addresses you want to send email to.

4. Run run.bat or run using an IDE.

