##hourspernight = int(input("How many hours per night do you sleep? "))

##hoursperweek = hourspernight * 7 

##print ("You sleep",hoursperweek,"hours per week") 

## The problem here is that hourspernight was a string and it needs to be an integer to use maths.

#hourspernight = int(input("How many hours per night do you sleep? "))

#hoursperweek = hourspernight * 7 

#print ("You sleep",str(hoursperweek),"hours per week") 

#hourspermonth = float(hoursperweek) * 4.35 

#print ("You sleep",str(hourspermonth),"hours per month") 

## The problem here is that string to real wasnt used in the print and u cant have an int and a string in one print without converting it.

dayspermonth = float(dayspermonth) / 24 

print ("This equates to",dayspermonth,"days per month") 