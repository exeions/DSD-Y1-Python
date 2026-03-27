import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4a.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return property sizes for a specific region')
    print('4) Return region with the highest overall increase in property value')
    print('5) Exit')
    return int(input(""))


def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    
    plt.show()
    return result

def region_highest_value_check():

    grouped = df.groupby("Region")[["Jan-19", "Sep-20"]].sum()
    grouped["Value Change"] = grouped["Sep-20"] - grouped["Jan-19"]

    highest_region = grouped["Value Change"].idxmax()
    highest_value = grouped["Value Change"].max()

    print(round(grouped, 2))
    print(f"Region with highest increase: {highest_region}")
    print(f"Increase amount: {round(highest_value, 2)}")

    # Create bar chart for ALL regions
    plt.figure(figsize=(8, 5))

    plt.bar(grouped.index, grouped["Value Change"])

    plt.title("Value Change by Region (Jan-19 to Sep-20)")
    plt.xlabel("Region")
    plt.ylabel("Value Change")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

x = mainmenu()
while x == 1 or x == 2 or x == 3 or x == 4:
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check: ")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20 ")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20 ")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")

    elif x == 3:  ## Region property size check
        while True:
            print()

            region = input("Please enter the name of the region you would like to check: ")
            region = region.capitalize()

            if region in df["Region"].values:
                while True:
                    property_type = input("Please enter the name of the property you would like to check: ")
                    property_type = property_type.capitalize()

                    if property_type in df["Property Type"].values:

                        # Filter dataset
                        filtered_df = df[(df["Region"] == region) & 
                                        (df["Property Type"] == property_type)]

                        if filtered_df.empty:
                            print("No data found for that selection.")
                            break
                        
                        total_rooms = filtered_df["Rooms"]
                        total_rooms_val = filtered_df["Rooms"].values

                        print(f"Total rooms in {region} for {property_type}: {total_rooms}")

                        # Create bar chart using the summed value
                        plt.figure(figsize=(6, 4))
                        plt.bar(total_rooms, total_rooms_val)

                        plt.title(f"Total Rooms for {property_type} in {region}")
                        plt.xlabel("Number of Homes")
                        plt.ylabel("Total Number of Rooms")
                        plt.tight_layout()
                        plt.show()

                        break
                    else:
                        print("Invalid property type.")
            else:
                print("Invalid region.")

    elif x == 4: ## Highest value region check
        region_highest_value_check()

    elif x == 5:
        break

    x = mainmenu()