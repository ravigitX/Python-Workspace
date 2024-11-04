from datetime import datetime
def getTwoDates():
    date1 = input("Enter the first date (dd/mm/yyyy): ")
    date2 = input("Enter the second date (dd/mm/yyyy): ")
    try:
        date1 = datetime.strptime(date1, "%d/%m/%Y")
        date2 = datetime.strptime(date2, "%d/%m/%Y")
    except ValueError:
        print("Incorrect date format. Please enter dates in 'dd/mm/yyyy' format.")
        return getTwoDates()
    if date1 > date2:
        date1, date2 = date2, date1

    return date1.year, date2.year

def isLeapYear(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

def leapNonLeapCount(start_year, end_year):
    leap_years = []
    non_leap_years = []
    for year in range(start_year, end_year + 1):
        if isLeapYear(year):
            leap_years.append(year)
        else:
            non_leap_years.append(year)
            
    return len(leap_years), len(non_leap_years), tuple(leap_years), tuple(non_leap_years)
def main():
    start_year, end_year = getTwoDates()
    leap_count, non_leap_count, leap_years, non_leap_years = leapNonLeapCount(start_year, end_year)
    year_frequency = {"Leap Years": leap_count, "Non-Leap Years": non_leap_count}
    print(f"Dates Entered: {start_year} - {end_year}")
    print("Leap Years:", leap_years)
    print("Non-Leap Years:", non_leap_years)
    print("Year Frequency:", year_frequency)

main()
