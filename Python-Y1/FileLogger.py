## Required inputs

name = input("Input name: ")
score = input("Input score: ")

## Validation

while not score.isdigit():
    print("Score is not in the correct format.")
    
    score = input("Input score: ")
else:
    print("Score value accepted!")

    ## View scores

    def viewScores():
        with open("scores.txt", "r") as file:
        
            ## Viewing scores

            view_scores = input("Would you like to view all previous scores? Y/N: ")
            if view_scores.lower() == "y":
                contents = file.readlines()

                print("".join(contents).strip())
            else:
                print("Closing program...")

            ## Range

            view_range = input("Would you like to view the highest and lowest scores? Y/N: ")
            if view_range.lower() == "y":
                scores = []

                for line in contents:
                    try:
                        score = int(line.strip().split(":")[1])
                        scores.append(int(score))
                    except:
                        pass
                if scores:
                    print(f"Highest score: {max(scores)}")
                    print(f"Lowest score: {min(scores)}")
                else:
                    print("No valid scores found")
            else:
                print("Closing program...")
                
            ## Average

            view_average = input("Would you like to view the average score? Y/N: ")
            if view_average.lower() == "y":
                scores = []

                for line in contents:
                    line = line.strip()
                    parts = line.split()
                    try:
                        score = int(parts[-1])
                        scores.append(score)
                    except:
                        pass
                if scores:
                    average_score = (sum(scores))/len(scores)
                    print(f"Average score: {round(average_score, 0)}")
                else:
                    print("No valid scores found")

            else:
                print("Closing program...")

    ## Write scores

    def writeScores():
        with open("scores.txt", "a") as file:
            file.write(f"{name}: {str(score)}\n")
            return score

    writeScores()
    
    viewScores()

