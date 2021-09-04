#file_to_load = "Resources/election_results.csv"
#with open(file_to_load) as election_data:
    #print(election_data)

#Add dependencies
import csv 
import os

#Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign variable to save file to path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read and print header row
    headers = next(file_reader) 
    print(headers)
    



#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Arapahoe\n")
    #txt_file.write("Denver\n")
    #txt_file.write("Jefferson")






election_data.close()
