from datetime import datetime, timedelta
def average_access_time(filename):
	with open(filename, 'r') as f:
		log={}
		for line in f:
			 date,time,userid,fileid,call= line.strip().split()
			 current = datetime.strptime(date + ' ' +time, '%H:%M:%S %m-%d-%Y')
			 if call =='open':
			 	if fileid in log:
			 		log[fileid][0] =current
			 	else:
			 		log[fileid]= [current,0]
			 elif call =='close':
			 	access_time =  current- log[fileid][0]
			 	log[fileid]= [current,access_time]
		
		sorted_dates= sorted(log.items(), key=lambda x:x[0][1])
		for fileid, access_time in sorted_dates:
			print(f'{fileid} {access_time[1]}')

average_access_time('file_access.txt')