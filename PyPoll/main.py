#main.py for pypoll
#import dependencies
import os
import csv

#create the path for file
pollpath = os.path.join('Resources', 'election_data.csv')


candidate_list = []
votes_per_candidate = []


#Read file
with open(pollpath, 'r') as pollfile:
    poll_file_reader = csv.reader(pollfile, delimiter=",")

    #Skip header row
    next(poll_file_reader)

    #Setup total vote count/names/total vote count per candidate
    overall_votes = 0
    percentage_votes = []
    


    for rows in poll_file_reader:
        
        candidate_names = rows[2]
        overall_votes = overall_votes + 1
        
        
        if candidate_names in candidate_list:
            candidates = candidate_list.index(candidate_names)
            votes_per_candidate[candidates] = votes_per_candidate[candidates] + 1
            
        else:
            candidate_list.append(candidate_names)
            votes_per_candidate.append(1)
            
            
    #Setup candidate percentages and the top vote that will be our winner
           
    winning_votes = votes_per_candidate[candidates]
    

    for totals in range(len(votes_per_candidate)):
        votes = round(votes_per_candidate[totals]/overall_votes * 100)
        percentage_votes.append(votes)

        

        if votes_per_candidate[totals] > winning_votes:
            winning_votes = votes_per_candidate[totals]
            top_candidate_votes = totals

        winning_candidate = candidate_list[top_candidate_votes]  

        
#Print all results    
print("Election Results")

print("-----------------------------------") 
       
print(f'Total Votes: {overall_votes}')
   
print("-----------------------------------")

for x in range(len(candidate_list)):
    print(f'{candidate_list[x]}: {percentage_votes[x]:.3f}% ({votes_per_candidate[x]})')

print("-----------------------------------")

print(f'Winner: {winning_candidate}')

print("-----------------------------------")

#Transfer to .txt file
text_file = os.path.join('Election_Results.txt')
with open (text_file, "w") as txt_converter:
    txt_converter.write("Election Results\n")

    txt_converter.write("-----------------------------------\n") 
       
    txt_converter.write(f'Total Votes: {overall_votes}\n')
   
    txt_converter.write("-----------------------------------\n")

    for x in range(len(candidate_list)):
        txt_converter.write(f'{candidate_list[x]}: {percentage_votes[x]:.3f}% ({votes_per_candidate[x]})\n')

    txt_converter.write("-----------------------------------\n")

    txt_converter.write(f'Winner: {winning_candidate}\n')

    txt_converter.write("-----------------------------------\n")

txt_converter.close()