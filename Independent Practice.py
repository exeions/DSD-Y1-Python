
def areaCalculator():
    base = float(input("Input the base of the rectangle (cm): "))
    height = float(input("Input the height of the rectangle (cm): "))

    a = base*height
    print(f"The area of your rectangle is {a}cm^2.")

def timeConverter():
    minsInput = float(input("Input your minutes: "))
    hour = minsInput // 60
    min = minsInput % 60

    print(f"{minsInput} is {hour} hours and {min} minutes")

def billingSystem():
    bill = input("Input bill (gbp): ")

    VAT = 1.05
    print(f"Your bill comes to {int(bill)*VAT} pounds")

