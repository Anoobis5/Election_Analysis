#1. The data we need to retrieve.
file_to_load='Desktop\Election_Analysis\Resources/election_results.csv'
    
import csv
import os
#Assign a variable for the file to load and the path
file_to_load =os.path.join("Resources","election_results.csv")


#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    file_reader=csv.reader(election_data)

    #Print the header row/
    headers = next(file_reader)
    print(headers)

    #Using the open() function with the "w" mode we will write the data to the file.
    with open(file_to_save,"w") as txt_file:
        #Write some data to the file.
        txt_file.write("Countiesn in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")




#2. The total number of votes cast.
#3. A complete list of candidates who received votes.
#4. The percentage of votes each candidate won.
#5. The total number of votes each candidate won.
#6. The winner of the election based on popular vote.   