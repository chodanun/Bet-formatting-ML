import csv

def writer(data):
    f = open("actor_score.csv","w")
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
				actor_1_name = str(row['actor_1_name'])
				actor_2_name = str(row['actor_2_name'])
				actor_3_name = str(row['actor_3_name'])
				gross = int(row['gross'])

				if gross != 0 :
					if dict_score.get(actor_1_name) == None :
						dict_score[actor_1_name] = gross
						dict_num[actor_1_name] = 1
					else :
						dict_score[actor_1_name] += gross
						dict_num[actor_1_name] += 1

					if dict_score.get(actor_2_name) == None :
						dict_score[actor_2_name] = gross
						dict_num[actor_2_name] = 1
					else :
						dict_score[actor_2_name] += gross
						dict_num[actor_2_name] += 1

					if dict_score.get(actor_3_name) == None :
						dict_score[actor_3_name] = gross
						dict_num[actor_3_name] = 1
					else :
						dict_score[actor_3_name] += gross
						dict_num[actor_3_name] += 1

			except (ValueError):
				pass

	data_input ="actor_name,actor_score"

	for key,value in dict_score.items():
		try:
			data_input += "\n%s,%d"%(key,value/dict_num[key])
		except (KeyError):
			data_input += "\n%s,%d"%(key,0)
		
	print (data_input)
	writer(data_input)

if __name__ == "__main__":
	main()