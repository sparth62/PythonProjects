import csv
import os 
import smtplib
from sys import argv
from email.message import EmailMessage
import imghdr

myFolder = 'images/' + argv[1]
fileList = [f for f in os.listdir(myFolder) if os.path.isfile(os.path.join(myFolder,f))]
#my_email_id = os.environ.get('my_email_id')							#SenderEmailId
my_email_id = 'sparth6299@gmail.com'							#SenderEmailId
#my_email_id_password = os.environ.get('my_email_id_password')				#SenderEmailIdPassword
my_email_id_password = '*******'				#SenderEmailIdPassword
participant_email_id = ''
input('Press any key to start')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	smtp.login(my_email_id,my_email_id_password)
	for i in fileList:
		msg = EmailMessage()
		msg['From'] = my_email_id
		msg['To'] = i.split('_')[1][:-4]
		msg['Subject'] = i.split('_')[0] + ' ISTE-Technothon 2k19 Registration Receipt'
		msg.set_content('Please Find the bellow attached Receipt. And keep with you in hardcopy during event. If you have any problem then contact Parth Shinojiya - 91043 99919')
		with open(myFolder +'/' + i, 'rb') as f:
			file_data = f.read()
			file_type = imghdr.what(f.name)
			file_name = f.name.split('/')[2].split('_')[0] + '.png'
			msg.add_attachment(file_data, maintype= 'image', subtype=file_type, filename=file_name)
			
		smtp.send_message(msg)
		print('Sent to ' + msg['To'])
		del msg
	smtp.quit()