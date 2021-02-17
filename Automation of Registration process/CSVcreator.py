import csv
from sys import argv
import_file_name = 'GoogleCSV/' + 'google_' + argv[1] + '.csv'
export_file_name = 'masterCSV/' + 'master_' + argv[1] + '.csv'

numeric_ref_no = int(argv[2])
#numeric_ref_no = 2001

l = []
with open(import_file_name, 'r') as ifile:
	reader_master = csv.reader(ifile, delimiter='|')
	for row in reader_master:
		if row[0] == 'Timestamp':
			l.append(['Ref No.', 'ISTE?', 'ISTE Number', 'Proof of ISTE Membership', 'Name', 'College Name', 'City', 'Email-ID', 'Mobile No', 'Event Category', 'EventName', 'participated_no','Fees Paid', 'Transection ID', 'Status', 'Remarks'])
		else:
			event_list = []
			if(row[8] != ''):
				temp = row[8].split(';')
				for k in temp:
					event_list.append('Biotechnology,' + k)
			if(row[9] != ''):
				temp = row[9].split(';')
				for k in temp:
					event_list.append('Chemical,' + k)
			if(row[10] != ''):
				temp = row[10].split(';')
				for k in temp:
					event_list.append('Civil,' + k)
			if(row[11] != ''):
				temp = row[11].split(';')
				for k in temp:
					event_list.append('Computer,' + k)
			if(row[12] != ''):
				temp = row[12].split(';')
				for k in temp:
					event_list.append('EC,' + k)
			if(row[13] != ''):
				temp = row[13].split(';')
				for k in temp:
					event_list.append('Electrical,' + k)
			if(row[14] != ''):
				temp = row[14].split(';')
				for k in temp:
					event_list.append('IT,' + k)
			if(row[15] != ''):
				temp = row[15].split(';')
				for k in temp:
					event_list.append('Mechanical,' + k)
			if(row[16] != ''):
				temp = row[16].split(';')
				for k in temp:
					event_list.append('Nanotechnology,' + k)
			for event in event_list:
				sub_l = []
				sub_l.append('Online - ' + str(numeric_ref_no))
				sub_l.append(row[18])
				sub_l.append(row[19])
				sub_l.append(row[20])
				sub_l.append(row[1])
				if(row[2] == 'Other'):
					sub_l.append(row[3])
				else:
					sub_l.append(row[2])
				#sub_l.append(row[4])
				if(row[4] == 'Other'):
					sub_l.append(row[5])
				else:
					sub_l.append(row[4])
				sub_l.append(row[6])
				sub_l.append(row[7])
				sub_l.append(event.split(',')[0])
				sub_l.append(event.split(',')[1])
				sub_l.append(row[17])
				if(row[18] == 'YES'):
					sub_l.append(row[21])
					sub_l.append(row[22])
				else:
					sub_l.append(row[23])
					sub_l.append(row[24])
				sub_l.append('')
				sub_l.append(row[0])
				l.append(sub_l)
			numeric_ref_no += 1
'''	
final_l = []
for i in l:
	final_sub = ''
	for j in i:
		final_sub += j + '|'
	final_l.append(final_sub)
'''
l.append(['Online - 0000','','','','','','','','','','','','','', 'Ok',''])
with open(export_file_name, mode='w',newline='') as efile:
	writer_master = csv.writer(efile, delimiter='|')
	for i in l:
		writer_master.writerow(i)