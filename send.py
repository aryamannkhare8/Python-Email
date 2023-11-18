'''
This is a python code that extracts name and column from the csv file. Then finds a pdf from the specified 
directory to extract the pdf file saved as 'name' with '.pdf' extension. If pdf exists then send a email,
if not then print the name for which no email was found.

'''

import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import glob


#function to extract names and email from csv
def extract_name_and_email(file_path):
    names = []
    emails = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append(row['Name'])
            emails.append(row['Email'])

    return names, emails

#function to attach pdfs and trigger the send_email function
def attach_pdfs(names, email_list):
    pdf_directory = 'copy path of pdf directory' #copy path of pdf directory

    for name, email in zip(names, email_list):
        pdf_files = glob.glob(f"{pdf_directory}/{name}*.pdf")
        if pdf_files:
            pdf_path = pdf_files[0]  # Assuming only one PDF per name
            send_email(name, email, pdf_path)
        else:
            print(f"No PDF found for {name}")

# Function to send email    
def send_email(name, recipient_email, pdf_path):
    sender_email = 'testing@github.com' #replace with sender's email
    sender_password = 'replace with your app password' #replace with your app password generated for your email

    
    message = MIMEMultipart()
    message['To'] = recipient_email
    message['From'] = sender_email
    message['Subject'] = 'This is the subject'  #Add Subject Here

    body = f"Hello {name},\n\nPlease find the attached PDF.\n\nRegards,\nYour Name" 
    message.attach(MIMEText(body, 'plain'))

    with open(pdf_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {pdf_path.split("/")[-1]}')

    message.attach(part)
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent to {recipient_email}")
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

file_path='emailListname.csv' #replace with name of the csv file which has two columns, "name" and "email"
names, emails = extract_name_and_email(file_path)

attach_pdfs(names, emails)

#to print the names and email in the csv
# for name, email in zip(names, emails):
#     print(f"Name: {name}, Email: {email}")   
