import hashlib

print("Welcome to the Voting System!")

# Create a dictionary to store the candidates and a list to store the votes
candidates = {
    "1": "Alice",
    "2": "Bob",
    "3": "Charlie"
}
votes = []

def hash_vote(name, candidate_id):
    # Hash the user's name combined with their chosen candidate ID using SHA-256
    vote_string = f"{name}_{candidate_id}"
    hashed_vote = hashlib.sha256(vote_string.encode()).hexdigest()
    return hashed_vote

# Main loop for the voting system
while True:
    print("\nPlease choose an option:")
    print("1. Vote for a candidate")
    print("2. View voting results")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nAvailable candidates:")
        for candidate_id, candidate_name in candidates.items():
            print(f"{candidate_id}. {candidate_name}")

        name = input("Enter your name: ")
        candidate_id = input("Enter the candidate ID you wish to vote for: ")

        if candidate_id in candidates:
            secure_vote = hash_vote(name, candidate_id)
            votes.append(secure_vote)
            print("Thank you for voting!")
        else:
            print("Invalid candidate ID.")
    
    elif choice == '2':
        vote_count = {candidate_id: 0 for candidate_id in candidates}

        for vote in votes:
            for candidate_id in candidates:
                if vote.endswith(f"_{candidate_id}"):
                    vote_count[candidate_id] += 1

        print("\nVoting Results:")
        for candidate_id, count in vote_count.items():
            print(f"{candidates[candidate_id]}: {count} votes")
    
    elif choice == '3':
        print("Thank you for using the Voting System. Goodbye!")
        break

    else:
        print("Incorrect input, please try again.")

