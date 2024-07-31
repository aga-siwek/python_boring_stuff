import re


def is_leap_year(year):
   if year % 4 == 0:
      if year % 400 == 0:
         return True
      elif year % 100 == 0:
         return False
      return True
   return False


def get_number_of_days_in_month(month, leap_year):
    if month == 2:
       return 29 if leap_year else 28

    return 31 if month % 2 != 0 else 30

   
def is_year_correct(year):
   return year >= 1000 and year <= 2999


def is_month_correct (month):
   return month >= 1 and month <= 12


def is_day_correct(day, month, year):
    leap_year = is_leap_year(year)
    number_of_days = get_number_of_days_in_month(month, leap_year)
    return day >=1 and day <= number_of_days
  

if __name__ == '__main__':
   date = "29/02/2000"
   date_regex = re.compile(r"(\d\d)/(\d\d)/(\d\d\d\d)")
   date_search = date_regex.search(date)
   day = int(date_search[1])
   month = int(date_search[2])
   year = int(date_search[3])
   leap_year = is_leap_year(year)

   print(f"day: {day}, month: {month}, year: {year}")
   print(f"Is it a leap year? {is_leap_year(year)} ")
   print(f"Is it a correct day? {is_day_correct(day, month, year)}")
   print(f"Is it a correct month? {is_month_correct(month)}")
   print(f"Is it a correct year? {is_year_correct(year)}")