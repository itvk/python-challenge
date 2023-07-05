import csv

file_to_load = r"C:\Users\kevin\AppData\Local\Temp\Temp1_pybank.zip\Starter_Code\PyPoll\Resources\election_data.csv"
file_to_output = r"C:\Users\kevin\Documents\GitHub\python-challenge\poll\poll.txt"
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_num = 0

with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)
    print(reader.fieldnames)
    for row in reader:
        total_votes += 1
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_output, 'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results)
    txt_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        votes_percentage = (votes / total_votes) * 100
        candidate_summary = f"{candidate}: {votes_percentage:.3f}% ({votes})\n"
        print(candidate_summary)
        txt_file.write(candidate_summary)

        if votes > winning_num:
            winning_num = votes
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
