import csv

zipList = []			#used for storing zip codes given
zipAndPopList = []		#used for storing zip codes and their population
finalList = []			#list that is written into the output file

def reading():
	print("Reading...")
	with open('givenZips.csv') as file:		#reads in a csv file; this file has one column and it's full of random zip codes
		reader = csv.reader(file)
		for row in reader:					#for each row in the csv file, store the random zips in zipList
			zipList.append(row)

	with open('zipAndPop.csv') as file:		#reads in a csv file; this file's 1st column is zips and a 2nd column i the population of that zip
		reader = csv.reader(file)
		for row in reader:					#for each row in the csv file, store the zips and their populations in zipAndPopList
			zipAndPopList.append(row)

def searching_and_writing():
	print("Searching...")
	with open('givenZipsO.csv','w') as oFile:		#prepares to write to a csv file called 'givenZipsO.csv' which is an exact copy of 'givenZips.csv'
		writer = csv.writer(oFile)
		with open('givenZips.csv','r') as file:		#allows for reading from 'givenZips.csv' so an index can be used once writing (line 35)
			reader = csv.reader(file)

			for i in zipList:	
				val = "Not Found"			#default value to be written if the population for a zip isn't found
				for j in zipAndPopList:
					if j[0] == i[0]:		#if a matching zip is found
						val = j[1]				#set val to the population
				finalList.append(val)		#appends val (which is either the population or 'Not Found')

			print("Writing...")
			count = 0
			for row in reader:
				row[1] = finalList[count]	#row[1] writes to 2nd column so it doesn't write over the zips in the 1st column
				writer.writerow(row)		#writes populations to 2nd column of 'givenZipsO.csv', right next to their respective zip code
				count+=1
	print("Complete!")
	
def main():
	reading()
	searching_and_writing()

main()