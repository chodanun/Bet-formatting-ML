import csv

def writer(data):
    f = open("director_score.csv","w")
    f.write(data)
    f.close()

def main():
	i = 0
	
	dict_score = {}
	dict_num = {}
	with open('mov_mm_train.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			try:
				director_name = str(row['director_name'])
				gross = int(row['gross'])

				if gross != 0 :
					if dict_score.get(director_name) == None :
						dict_score[director_name] = gross
						dict_num[director_name] = 1
					else :
						dict_score[director_name] += gross
						dict_num[director_name] += 1

			except (ValueError):
				pass

	data_input ="director_name,director_score"
	no = 0
	for key,value in dict_score.items():
		try:
			data_input += "\n%s,%d"%(key,value/dict_num[key])
		except (KeyError):
			data_input += "\n%s,%d"%(key,0)
		no+=1
	print (no)
	print (data_input)
	writer(data_input)

if __name__ == "__main__":
	main()