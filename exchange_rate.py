import csv
from easymoney.money import EasyPeasy
ep = EasyPeasy(fuzzy_threshold=True)
attrs = ['color','director_name','num_critic_for_reviews','duration','director_facebook_likes','actor_3_facebook_likes','actor_2_name','actor_1_facebook_likes','movie_facebook_likes','genres','actor_1_name','movie_title','num_voted_users','cast_total_facebook_likes','actor_3_name','facenumber_in_poster','plot_keywords','movie_imdb_link','num_user_for_reviews','language','country','content_rating','budget','title_year','actor_2_facebook_likes','imdb_score','aspect_ratio','gross']

def formatingExchangeRate(amount,region,from_year):

	try:
		money = ep.currency_converter(amount, region, to_currency="Germany")
	except (Exception):
		money = 0 
	return money

def writer(data):
    f = open("newfile.csv","w")
    f.write(data)
    f.close()

def main():
	i = 0
	data_input ="id,gross2016"
	with open('mov_mm_train.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			try:
				amount_reader = int(row['gross'])
				region_reader = row['country']
				from_year_reader = int(row['title_year'])
				id_reader = row['id']

				new_gross = formatingExchangeRate(amount_reader, region_reader, from_year_reader)
				data_input += "\n%s,%d"%(str(id_reader),int(new_gross))
				i+=1
				print (i)
			except (ValueError):
				pass
	writer(data_input)
			# money = str(row['gross']).split(' ')
			# money = money[0].replace(",","")
			# print (money)
			


if __name__ == "__main__":
	main()