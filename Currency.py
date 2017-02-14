import csv
from easymoney.money import EasyPeasy
ep = EasyPeasy(fuzzy_threshold=True)

attr = ['color','director_name','num_critic_for_reviews','duration','director_facebook_likes','actor_3_facebook_likes','actor_2_name','actor_1_facebook_likes','movie_facebook_likes','genres','actor_1_name','movie_title','num_voted_users','cast_total_facebook_likes','actor_3_name','facenumber_in_poster','plot_keywords','movie_imdb_link','num_user_for_reviews','language','country','content_rating','budget','title_year','actor_2_facebook_likes','imdb_score','aspect_ratio','gross']
# attr = [['color',1],['director_name',1],['num_critic_for_reviews',0],['duration',0],['director_facebook_likes',0],['actor_3_facebook_likes',0],['actor_2_name',1],['actor_1_facebook_likes',0],['movie_facebook_likes',0],['genres',1],['actor_1_name',1],['movie_title',1],['num_voted_users',0],['cast_total_facebook_likes',0],['actor_3_name',1],['facenumber_in_poster',0],['plot_keywords',1],['movie_imdb_link',1],['num_user_for_reviews',0],['language',1],['country',1],['content_rating',1],['budget',0],['title_year',0],['actor_2_facebook_likes',0],['imdb_score',0],['aspect_ratio',0],['gross',0]]
def convertMoney(amount,country,year):
	# money = ep.currency_converter(amount=amount, from_currency=country, to_currency="USD")
	# return ep.normalize(amount=int(money), region="USA", from_year=year, to_year="latest")
	return ep.currency_converter(amount=amount, from_currency=country, to_currency="USD")

def write_file(data, filename):
    f = open(filename, 'w')
    f.write(data)
    f.close()
    return True

def main():
	Ans = "color,director_name,num_critic_for_reviews,duration,director_facebook_likes,actor_3_facebook_likes,actor_2_name,actor_1_facebook_likes,movie_facebook_likes,genres,actor_1_name,movie_title,num_voted_users,cast_total_facebook_likes,actor_3_name,facenumber_in_poster,plot_keywords,movie_imdb_link,num_user_for_reviews,language,country,content_rating,budget,title_year,actor_2_facebook_likes,imdb_score,aspect_ratio,gross\n"
	error_row = []
	with open('mov_mm_train.csv', 'rb') as csvfile:
		i = 1
		gdpreader = csv.DictReader(csvfile)
		for row in gdpreader:
			print (i)
			i += 1
			if row['gross'] != '':
				if row['budget'] != '' and row['title_year'] != '' and row['country'] != '':
					try:
						row['budget'] = convertMoney(int(row['budget']), row['country'], int(row['title_year']))
						try:
							row['gross'] = convertMoney(int(row['gross']), row['country'], int(row['title_year']))
						except:
							pass
					except Exception as e:
						error_row.append(i)
				if row['title_year'] != '':
					row['title_year'] = int(row['title_year'])-1916
				for att in attr:
					row[att] = str(row[att]).replace(",", "")
					if att != 'gross' and str(row[att]) != "":
						Ans += str(row[att]) + ','
					elif str(row[att]) == "":
						Ans += '?,'
					else:
						Ans += str(row[att])
				Ans += '\n'
	write_file(Ans,'test2.csv')
	print (error_row)
	print ("num : " + str(len(error_row)))

if __name__ == '__main__':
	main()


