import pandas as pd
import matplotlib.pyplot as plt

## add:
# sales of different categories of products
# income and profit made on different products

#Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Sales of different categories of products")
        print("3. Income and profit made on different products")

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            flag = True

    return int(choice)

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():

    df = pd.read_csv("20251128_Digital_DSD_AdSAM_Core_ESP_Task_4a_RetailX_data_V0.1.csv")

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

def sales_by_category ():
    
    df = pd.read_csv("20251128_Digital_DSD_AdSAM_Core_ESP_Task_4a_RetailX_data_V0.1.csv")

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    df["Week"] = df["Date"].dt.isocalendar().week

    grouped = df.groupby(["Week", "Category"])["Qty Sold"].sum()
    grouped = grouped.unstack()
    print(grouped)

    grouped.plot(kind="bar")
    plt.title("Sales by Category Over Time")
    plt.xlabel("Weeks")
    plt.ylabel("Sales")

    plt.show()

def income_and_profit():

    df = pd.read_csv("20251128_Digital_DSD_AdSAM_Core_ESP_Task_4a_RetailX_data_V0.1.csv")
    
    df["Sales Price"] = pd.to_numeric(df["Sales Price"])
    df["Cost Price"] = pd.to_numeric(df["Cost Price"])

    df["Income"] = df["Qty Sold"] * df["Sales Price"]
    df["Total Cost"] = df["Qty Sold"] * df["Cost Price"]
    df["Profit"] = df["Income"] - df["Total Cost"]

    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    df["Week"] = df["Date"].dt.isocalendar().week

    summary = df.groupby(["Week", "Product ID"])[["Income", "Profit"]].sum()
    print(summary)

    summary.plot(kind="bar")
    plt.xticks(rotation=90)
    plt.ylabel("Amount")
    plt.show()



#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("20251128_Digital_DSD_AdSAM_Core_ESP_Task_4a_RetailX_data_V0.1.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))
    
    date_ID["Date"] = pd.to_datetime(date_ID["Date"])

    grouped = date_ID.groupby("Date")["Qty Sold"].sum()
    grouped.plot(kind="line")
    plt.xlabel("Date")
    plt.ylabel("Qty Sold")
    plt.show()

main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)

if main_menu_choice == 2:
    sales_by_category()

if main_menu_choice == 3:
    income_and_profit()