i = 20
def test():
	global i
	i += 1

def main():
	a = "test"
	b = "01"
	data =""
	data += "'%s','%s'\n"%(a,b)
	print (data)

if __name__ == '__main__':
	main()