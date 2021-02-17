from selenium import webdriver
import time
import csv
driver = webdriver.Chrome('g:/bot/chromedriver')
l_main=[['Enrollment_Number','Name','DE-IIB','SE','JAVA','WT','.Net','DCDR','SPI','CPI','Backlog']]
driver.get('https://www.gturesults.in/Default.aspx')
l_seat=["150470116001","150470116002"]#,"160470116003","160470116004","160470116005","160470116006","160470116007","160470116008","160470116009","160470116010","160470116011","160470116012","160470116013","160470116014","160470116015","160470116016","160470116017","160470116018","160470116019","160470116020","160470116021","160470116022","160470116023","160470116024","160470116025","160470116026","160470116027","160470116028","160470116029","160470116030","160470116031","160470116032","160470116033","160470116034","160470116035","160470116036","160470116037","160470116038","160470116039","160470116040","160470116041","160470116042","160470116043","160470116044","160470116045","160470116046","160470116047","160470116048","160470116049","160470116050","160470116052","160470116054","160470116055","160470116056","160470116057","160470116058","160470116059","160470116060","160470116061","160470116062","160470116066","170473116001","170473116002","170473116003","170473116004","170473116005","170473116006"]
input()
for i in range(len(l_seat)):
	l_sub=[]
	number = driver.find_element_by_name("txtenroll")
	number.clear()
	number.send_keys(l_seat[i])
	captcha=driver.find_element_by_name("CodeNumberTextBox");
	captcha.click();
	time.sleep(10)
	submit= driver.find_element_by_name("btnSearch")
	submit.click()
	time.sleep(0.5)
	seat_name=driver.find_element_by_id("lblEnrollmentNo").text
	l_sub.append(seat_name)
	name=driver.find_element_by_id("lblName").text
	l_sub.append(name)
	m1=driver.find_element_by_xpath("//div[@id='tblMR_DI']/table[2]/tbody/tr/td[6]").text
	l_sub.append(m1)
	m2=driver.find_element_by_xpath("//div[@id='tblMR_DI']/table[2]/tbody/tr[2]/td[6]").text
	l_sub.append(m2)
	m3=driver.find_element_by_xpath("//div[@id='tblMR_DI']/table[2]/tbody/tr[3]/td[6]").text
	l_sub.append(m3)
	m4=driver.find_element_by_xpath("//div[@id='tblMR_DI']/table[2]/tbody/tr[4]/td[6]").text
	l_sub.append(m4)
	m5=driver.find_element_by_xpath("//div[@id='tblMR_DI']/table[2]/tbody/tr[5]/td[6]").text
	l_sub.append(m5)
	m6=driver.find_element_by_xpath("//div[@id='tblMR_DI']/table[2]/tbody/tr[6]/td[6]").text
	l_sub.append(m6)
	spi=driver.find_element_by_id("lblSPI").text
	l_sub.append(spi)
	cpi=driver.find_element_by_id("lblCPI").text
	l_sub.append(cpi)
	Backlog=driver.find_element_by_id("lblCUPBack").text
	l_sub.append(Backlog)
	l_main.append(l_sub)

myFile = open('analysis_GTU.csv', 'a',newline='')  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(l_main)
	