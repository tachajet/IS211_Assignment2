def downloadData(url):
#Part 2: function to download data from the web
	import urllib.request
	web_var=urllib.request.urlopen(url)
	return web_var
def processData(bday_var):
#Part 3: function to take data from Part 2 and process it into a dictionary, with logging set up
	import csv
	import io
	import datetime
	import logging
	logging.basicConfig(filename='error.log',filemode='w',level=logging.ERROR)
	bday_csv=csv.reader(io.TextIOWrapper(bday_var))
	date_dict={}
	line_cnt=-1
	next(bday_csv)
	for line in bday_csv:
		line_cnt+=1
		try:
			bday_date=datetime.datetime.strptime(line[2],'%d/%m/%Y').date()
			date_dict[line[0]]=(line[1],bday_date)
		except:
			logging.error("Error processing line %i for ID %s",line_cnt, line[0])
	return date_dict
def displayPerson(ident,personData):
#Part 4: function to look up data from Part 3's dictionary 
	if str(ident) in personData.keys():
		print("Person",str(ident) +" is", personData[str(ident)][0] + " with a birthday of",personData[str(ident)][1])
	else:
		print("Not found")
def main():
#Part 5: main function, tying everything together and providing user interface and input capability
	import argparse
	parser=argparse.ArgumentParser()
	parser.add_argument('--url', type=str)
	args=parser.parse_args()
	pass_url=downloadData(args.url)
	bday_info=processData(pass_url)
	id_num=input("Please enter an ID number: ")
	if int(id_num)<=0:
		exit()
	else:
		displayPerson(id_num,bday_info)
if __name__=="__main__":
	main()
		
