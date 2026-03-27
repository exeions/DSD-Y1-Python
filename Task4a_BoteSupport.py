import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time for issue to be resolved")
        print("### 3. Issues and resolutions by region")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg


def get_resolution_trends(issue_type):
    
    issues = pd.read_csv("Task4a_data.csv")

    # Filter to selected issue type

    filtered_issues = issues[issues['Issue Type'] == issue_type]

    if filtered_issues.empty:
        print(f"No data found for issue type: {issue_type}")
        return

    # Calculate totals and averages

    trends = filtered_issues['Days To Resolve'].agg(
        Total_Days='sum',
        Average_Days='mean'
    )

    print("####################################################")
    print(f"### Time Taken to Resolve: {issue_type} ###")
    print("####################################################")
    print(trends)

    # Plot days to resolve per issue (using index as x-axis)
    
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_issues.index, filtered_issues['Days To Resolve'], marker='o')
    plt.title(f"Days to Resolve Issues – {issue_type}")
    plt.xlabel("Issue Index")
    plt.ylabel("Days to Resolve")
    plt.grid(True)
    plt.show()

def issues_by_region():
    issues = pd.read_csv("Task4a_data.csv")

    # Bar chart

    region_resolutions = pd.crosstab(
        issues['Region'],
        issues['How Resolved']
    )

    region_resolutions.plot(
        kind='bar',
        stacked=False,
        figsize=(10, 6)
    )

    plt.title("How Issues Were Resolved by Region")
    plt.xlabel("Region")
    plt.ylabel("Number of Issues")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

main_menu_choice = main_menu()
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))
elif main_menu_choice == "2":
    issue_type_choice = total_menu()
    get_resolution_trends(issue_type_choice)
elif main_menu_choice == "3":
    issues_by_region()