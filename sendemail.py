import smtplib
from email.message import EmailMessage
import csv
import time
import datetime

current_time = datetime.datetime.now()

def is_within_time_window():
    now = datetime.datetime.now()
    return now.time() >= datetime.time(8, 0) and now.time() <= datetime.time(17, 0)

# Open a text file to save the print statements
log_file = open("logs.txt", "a")

# Load the college data from the CSV file
with open("data.csv", 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        try:
            if not is_within_time_window():
                # If it's outside the time window, pause the script
                while not is_within_time_window():
                    time.sleep(60)  # Sleep for 60 seconds (1 minute)

            # Create an EmailMessage object
            email = EmailMessage()

            # Set the sender's email and password
            sender_email = 'GMAIL EMAIL'
            sender_password = 'APP PASSWORD'

            # Set the sender's information
            email['from'] = 'FIRST LAST NAME'

            # Set the receiver's email id
            receiver_email = row['Email']  # Assuming 'Email' is the column name in the CSV file
            email['to'] = receiver_email

            # Set the subject
            email['subject'] = f'Request for {row["Name of College"]} Merchandise as a High School Senior'

            # Set the content of the email with placeholders replaced
            message = f"""
Dear {row["Name of College"]} admissions,

I hope this message finds you well. I am writing to express my excitement and interest in {row["Name of College"]} while I'm in my final year of high school. I have been researching colleges, and this school has stood out to me for its great academic programs, vibrant campus life, and strong sense of community.

As a high school senior, I am now wanting to represent this school with some merch. I think that displaying some college merch could be fun with my friends. I am reaching out to kindly request if it would be possible to receive some college merchandise, such as t-shirts, hats, or other promotional items that I could wear and showcase.

I understand that college merchandise is a great way to connect with prospective students, and I would love to show off my prospective college to my high school.

If it is possible to send some college merchandise my way, I would be extremely grateful. My information is at the bottom, thank you for considering.

Sincerely,
FIRST LAST NAME

FULL ADDRESS
"""
            email.set_content(message)

            # Send the email
            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                smtp.ehlo()  # Identify yourself to an ESMTP server using EHLO
                smtp.starttls()  # Put the SMTP connection in TLS (Transport Layer Security) mode
                smtp.login(sender_email, sender_password)  # Sender's email ID and password
                smtp.send_message(email)
                current_time = datetime.datetime.now()
                log_message = f'Email sent to {row["Name of College"]} ({receiver_email}) at {current_time}'
                print(log_message)
                log_file.write(log_message + '\n')

            # Wait for 200 seconds before sending the next email
            time.sleep(200)
            
        except Exception as e:
            current_time = datetime.datetime.now()
            error_message = f'Error sending email to {row["Name of College"]} ({receiver_email}): {e} at {current_time}'
            print(error_message)
            log_file.write(error_message + '\n')

# Close the log file
log_file.close()
