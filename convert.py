import csv

f1 = open("mov_mm_train-2.csv","r").read()
f2 = open("movie_metadata.csv","r").read()
f3 = open("test_set.csv","w")

# reader_f1 = csv.DictReader(f1)
# reader_f2 = csv.DictReader(f2)
data = "color,director_name,num_critic_for_reviews,duration,director_facebook_likes,actor_3_facebook_likes,actor_2_name,actor_1_facebook_likes,gross,genres,actor_1_name,movie_title,num_voted_users,cast_total_facebook_likes,actor_3_name,facenumber_in_poster,plot_keywords,movie_imdb_link,num_user_for_reviews,language,country,content_rating,budget,title_year,actor_2_facebook_likes,imdb_score,aspect_ratio,movie_facebook_likes\n"

i = 0
f1 = f1.split('\n')
f2 = f2.split('\n')
for row in f2:
	check_re = False
	for row2 in f1:
		if (row2 == row):
			check_re = True
	if check_re == False :
		data += row+'\n'
		i+=1
# print (data)
f3.write(data)
print (i)
# f3.write(data)
# f3.close()

