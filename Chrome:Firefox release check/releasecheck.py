import datetime
import os
import time
import re
from datetime import date
import dateutil.parser as dparser
import smtplib, ssl
import smtplib
from email.message import EmailMessage



def checkdates (dateString,todaysdatef,chrome_check,ff_check):
    

    desktop_path = os.path.normpath(os.path.expanduser("~/Desktop"))
    
    chrome_filename = desktop_path+"/Chrome:Firefox release check/chromereleases.txt"

    with open(chrome_filename) as chrome_file:

        for chrome_line in chrome_file:
            chrome_match = re.search(r'\d{4}-\d{2}-\d{2}', chrome_line)
            chrome_date = str(datetime.datetime.strptime(chrome_match.group(), '%Y-%m-%d').date())
            chromeDateString = datetime.datetime.strptime(chrome_date,'%Y-%m-%d').isocalendar()[1]
            chrome_first_chars = str(todaysdatef)[0:4]
            first_chrome_chars = str(chrome_date)[0:4]

            if (dateString == chromeDateString and int(chrome_first_chars) == int(first_chrome_chars)):
                    chrome_version = chrome_line[-21:]
                    chrome_release_date = chrome_line[0:10]
                    print(chrome_version.strip() + " is released on " + chrome_release_date)
                    chrome_check = 1
                    print(chrome_check)

    
    filename = desktop_path+"/Chrome:Firefox release check/firefoxreleases.txt"

    with open(filename) as file:
        
        for line in file:
            match = re.search(r'\d{4}-\d{2}-\d{2}', line)
            date = str(datetime.datetime.strptime(match.group(), '%Y-%m-%d').date())
            ffDateString = datetime.datetime.strptime(date,'%Y-%m-%d').isocalendar()[1]
            first_chars = str(todaysdatef)[0:4]
            first_ff_chars = str(date)[0:4]
            
            if (dateString == ffDateString and int(first_chars) == int(first_ff_chars) ):
                    version = line[-22:]
                    release_date = line[0:10]
                    print(version.strip() + " is released on " + release_date) 
                    ff_check = 1
                    print(line)                   
                    print(ff_check)
                    
    email_address = "filesignotification@gmail.com"
    email_password = "npinsmefwbsxsxuj"
    # create email
    msg = EmailMessage()
    msg['Subject'] = "Releases"
    msg['From'] = email_address
    msg['To'] = "jmcateer@flexera.com, hsingh@flexera.com"


                    
    if ( chrome_check == 1 and ff_check == 1):
        print("Send Email")
        print(version.strip() + " is released on " + release_date) 
        msg.set_content("This is an automated email message. Upcoming releases:" + "\n" + version.strip() + " is released on " + release_date + "\n" + chrome_version.strip() + " is released on " + chrome_release_date)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    elif (ff_check == 1 and chrome_check == 0):
        print("Send FF Email")

        msg.set_content("This is an automated email message. Upcoming releases:" + "\n" + version.strip() + " is released on " + release_date)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    elif (chrome_check and 1 & ff_check == 0):
        print("Send Chrome Email")

        msg.set_content("This is an automated email message. Upcoming releases:" + "\n" + chrome_version.strip() + " is released on " + chrome_release_date)

        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    elif (chrome_check == 0 and 0 & ff_check == 0):
        print("Do not send Email")
    


            
                    
            
print("------------------------------------")
print("Chrome/Firefox release dates checker")
print("------------------------------------")
print('\n')

time.sleep(0.5)

#Establishing Global Variables
todaysdate = date.today()
todaysdatef = todaysdate.strftime("%Y-%m-%d")
dateString = datetime.datetime.strptime(todaysdatef,'%Y-%m-%d').isocalendar()[1]
chrome_check = 0
ff_check = 0

checkdates(dateString,todaysdatef,chrome_check,ff_check)

