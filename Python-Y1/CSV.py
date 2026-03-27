import csv
import os 

FILENAME = "scores.csv"

if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([" usernames ", " scores "])
        print("Inserted headers!")
else:
    print("File already has content.")

def add_score(username, score):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])
        

def show_scores():
    with open(FILENAME, "r", newline="") as file:
        contents = file.read()
        print(contents.strip())

def leaderboard():
    scores = []

    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row

        for row in reader:
            if row:
                username = row[0]
                score = int(row[1])
                scores.append((username, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    print(*scores)

def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Leadboard")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            if score >= 0 and score <= 100:
                add_score(username, score)
            else:
                print("Score is out of range, please input data between 0-100")
        elif choice == "2":
            show_scores()
        elif choice == "3":
            leaderboard()
        elif choice == "4":
            print("Goodbye!")
            break
       
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()