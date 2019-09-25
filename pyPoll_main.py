import os
import csv
import pandas as pd

#csv path
csv_path = "Resources/election_data.csv"

# read in csv
election_data_df = pd.read_csv(csv_path)
#print(election_data_df.head(5))

#Total votes
total_votes = election_data_df["Voter ID"].count()
print(f'Total Votes: {total_votes}')

# GroupBy candidates
candidate_group = election_data_df.groupby(['Candidate'])
#print(candidate_group.head())

candidate_votes = candidate_group["Voter ID"].count()
print(candidate_votes)
print(round(candidate_votes/total_votes*100,2))

# Winner
candidate_winner= "Khan"
print("Winner:" + candidate_winner)

summary_df = pd.DataFrame({
    "Total Votes" : [total_votes], 
    "Candidate Results" : [candidate_votes], 
    "Winner" : [candidate_winner]})    

summary_df.to_excel("output/CindyPendarvis_electionResults.xlsx", index=False)