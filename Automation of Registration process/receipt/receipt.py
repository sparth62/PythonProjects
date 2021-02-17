from selenium import webdriver
from sys import argv
import csv
import time
import os
baseURL = "C:/Users/parthShinojiya/Desktop/ISTE2k19/receipt/"
driver = webdriver.Chrome(baseURL + 'browser_driver/chromedriver')
driver.set_window_size(725,440) #(width,hight)
driver.get(baseURL + 'receipt.html')
file_name = 'CSVFiles/' + argv[1] + '.csv'
form_date = argv[1]
#file_name = 'CSVFiles/' + input("Enter csv file name with extension:")
#form_date = input("Enter date for form like, 31-08-2019 :")
os.mkdir(baseURL + 'images/' + form_date)

participated_no = 0
previous_sr_no = 'initial'
iste_number = ''
name = ''
mobile_no = ''
total_amount = ''
email = ''
#input('Press any key to start')

with open(file_name, 'r') as csvfile:
	reader_master = csv.reader(csvfile, delimiter='|')
	for row in reader_master:
		status = row[14] #12
		if status == 'Ok-2':
			sr_no = row[0]
			if sr_no == previous_sr_no:
				participated_no += 1
				event_name = row[10] #9
				event_element_name = 'event' + str(participated_no)
				event_name_element = driver.find_element_by_name(event_element_name)
				event_name_element.send_keys(event_name)
			else:
				participated_no_element = driver.find_element_by_name('participated_no')
				participated_no_element.send_keys(participated_no)
				total_amount_element = driver.find_element_by_name('total_amount')
				total_amount_element.send_keys(total_amount)
				header_element=driver.find_element_by_name('header')
				header_element.click()
				ss_name = previous_sr_no+ '_' + email
				#ss_name = previous_sr_no
				driver.save_screenshot('images/' + form_date + '/' + str(ss_name) + ".png")

				date_element = driver.find_element_by_name('date')
				date_element.clear()
				sr_no_element = driver.find_element_by_name('srno')
				sr_no_element.clear()
				name_element = driver.find_element_by_name('name')
				name_element.clear()
				mobile_no_element = driver.find_element_by_name('mobile')
				mobile_no_element.clear()
				iste_number_element = driver.find_element_by_name('iste_no')
				iste_number_element.clear()
				event_name_element = driver.find_element_by_name('event1')
				event_name_element.clear()
				driver.find_element_by_name('event2').clear()
				driver.find_element_by_name('event3').clear()
				driver.find_element_by_name('event4').clear()
				driver.find_element_by_name('event5').clear()
				driver.find_element_by_name('event6').clear()
				participated_no_element.clear()
				total_amount_element.clear()

				previous_sr_no = sr_no
				participated_no = 1
				name = row[4] #3
				email = row[7] #6
				mobile_no = row[8] #7
				iste_number = row[2] #2
				event_name = row[10] #9
				total_amount = row[12] #10

				date_element.send_keys(form_date)
				sr_no_element.send_keys(sr_no)
				name_element.send_keys(name)
				mobile_no_element.send_keys(mobile_no)
				iste_number_element.send_keys(iste_number)
				event_name_element.send_keys(event_name)
os.remove('images/' + form_date + '/initial_.png')