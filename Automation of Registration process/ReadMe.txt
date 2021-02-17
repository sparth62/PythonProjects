Step - 1 : download csv file from google form and rename it as 'google_05-09-2019.csv'and put it into 'GoogleCSV',
Step - 2 : open file from GoogleCSV and 'find and replace' ',' with '|' and  Delete old entries, save it
Step - 3 : run CSVcreator.py :   python CSVcreator.py 05-09-2019 1001
Step - 4 : open file from MasterCSV and save as 'master_05-09-2019.xlsx'
Step-  5 : Now set column width and Format(number) of field [ISTE no,Mobile no, Transection ID] and Verify all the things.and remove extra spaces from mobile no,....
Step - 6 : Save as .xlsx file in receipt/CSVfiles '05-09-2019.csv' (CSV Comma Delimited) 
Step - 7 : run receipt.py > python receipt.py 05-09-2019
Step - 8 : verify random receipt. saved in images/05-09-2019 
Step - 9 : run send_email.py > python send_email.py 05-09-2019