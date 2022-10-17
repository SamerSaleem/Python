#import csv module in order to read it and parse it
import csv

#open the csv, note if you use "with open" you can iterate through csv data and display information.
samplefile = open("parsing.csv")
#read the csv using reader object
samplereader= csv.reader(samplefile)
#display as a list using the list function
sampledata= list(samplereader)
#print the list 
print(sampledata)