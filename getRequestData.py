# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests
from sourcedata import get_file_data
import datetime
#requests.packages.urllib3.disable_warnings()

def f_time(time):
    time = time.replace('T',' ')
    time =  time.split('.')[0]
    return time

def t_elapsed(start, finish):
	r_start = f_time(start)
	r_end = f_time(finish)
	r_time = (datetime.datetime.strptime(r_end, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(r_start, '%Y-%m-%d %H:%M:%S'))
	mm_ss = divmod(r_time.total_seconds(),60)
	return mm_ss 

def is_yday(s_time):
	yday = datetime.datetime.now() - datetime.timedelta(days = 1)
	date_yday = yday.strftime('%Y-%m-%d')
	return (date_yday in s_time)
	
def get_request_data():
	source = get_file_data('requestData.json')
	for request in source['content']:
		if is_yday(request['dateSubmitted']): 
			if request['@type'] == 'CatalogItemRequest':
				if request['state'] == 'SUCCESSFUL':
						print (
						request['id'],
						request['requestedItemName'],
						request['requestedFor'],
						request['organization']['subtenantLabel'],
						t_elapsed(request['dateSubmitted'],request['dateCompleted'])
					)

if __name__ == "__main__":
	get_request_data()

