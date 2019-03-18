# -*- coding: utf-8 -*-
import yaml
import time
import argparse

from monitor import Monitor

# doc: python main.py --city=BAB

if __name__ == '__main__':

	with open("config.yml", 'r') as f:
		config = yaml.load(f)

	parser = argparse.ArgumentParser()
	parser.add_argument('--city', metavar='city', type=unicode, help='city')
	args = parser.parse_args()

	# for city_data in config['data']: # TODO
	city_data = config['data']
	city_data = [item for item in city_data if item['city'] == args.city][0]
	# BAB = Monitor(city_data[0])
	BAB = Monitor(city_data)

	BAB.init_posts()
	# idf.init_posts()
	
	while True:	
		BAB.monitor_change()
		time.sleep(60 * city_data['frequency'])
