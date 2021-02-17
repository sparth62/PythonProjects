from selenium import webdriver

driver = webdriver.Chrome('G:\\root\\Projects\\KBC_CPP\\chromedriver')
driver.get('https://web.whatsapp.com/')
print("Select your friend:\n1.Kishorbhai Shinojiya\n2.Pathu")
name = input('Enter friend name:')
msg = 'Hi, I am Parth Shinojiya from "KAUN BANEGA CROREPATI", Your friend need your help. Please help him...'
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')
msg_box.send_keys(msg)
button = driver.find_element_by_class_name('_2lkdt')
button.click()