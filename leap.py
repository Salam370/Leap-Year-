# Code your functions here!

# 1. Write a function that checks to see if a given year is a leap year, by replacing "pass" with your own code, and returns either the boolean value True or False.
def is_leap_year(year):
   return(year%4==0)
print(is_leap_year(1990))
print(is_leap_year(1992))
 


# 2. Write a function that takes in the current year and returns a string telling when the next leap year will be.
def next_leap_year(current_year):
    if current_year % 4 == 0:
        return "This year is a leap year"
    while current_year % 4 != 0:
        current_year=current_year+1
    return current_year 
print(next_leap_year(2019))

# 3. Write a function that takes in two years as arguments (a start_year and a last_year), and then prints out every single year between them that is a leap year. 
