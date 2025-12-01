name = input("Input name: ")
score = int(input("Input score: "))

## View scores
def viewScores():
    with open("scores.txt", "r") as file:
        contents = file.readlines()

        print("".join(contents).strip())

        view_range = input("Would you like to view the highest and lowest scores? Y/N: ")
        if view_range.lower() == "y":
            scores = []

            for line in contents:
                try:
                    score = int(line.strip().split(":")[1])
                    scores.append(score)
                except:
                    pass
            if scores:
                print(f"Highest score: {max(scores)}")
                print(f"Lowest score: {min(scores)}")
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

view_scores = input("Would you like to view all previous scores? Y/N: ")
if view_scores.lower() == "y":
    viewScores()
else:
    print("Closing program...")