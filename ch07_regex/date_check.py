#DD/MM/RRRR day 0-31, month 01-13 year 1000-2999

import re
date = "31/02/2998"
# days = re.compile(r"\d\d")
# months = re.compile(r"/\d\d/")
# years = re.compile(r"(\d){4}")

def months_finder (date):
   months = re.compile(r"/(0[1-9])/|/(1[0-2])/") 
   month = months.search(date[2:6])
   month = int(int(month.group()[1:3]))
   return month

def years_finder (date):
  years = re.compile(r"[1-2][0-9][0-9][0-9]")
  year = years.search(date[6:])
  year = year.group()
  return year

def leap_year_finder (year):
   if year % 4 == 0:
      if year % 400 == 0:
         return True
      elif year % 100 == 0:
         return False
      return True


def days_finder (date, month):
    if month == 4 or month== 6 or month == 9 or month == 11:

        days =  re.compile(r"0\d|1\d|2\d|30|")
        day = days.search(date[:2])
        day = int(day.group())
        return day
    elif month == 2:
        if leap_year_finder == True:
            days =  re.compile(r"0\d|1\d|2[0-9]")
            day = days.search(date[:2])
            day = int(day.group())
            return day
        else:
            days =  re.compile(r"0\d|1\d|2[0-9]")
            day = days.search(date[:2])
            day = int(day.group())
            return day
    else:
        days =  re.compile(r"0\d|1\d|2\d|30|31")
        day = days.search(date[:2])
        day = int(day.group())
        return day
       



def years_finder (date):
  years = re.compile(r"[1-2][0-9][0-9][0-9]")
  year = years.search(date[6:])
  year = year.group()
  return year


    
# days =  re.compile(r"0\d|1\d|2\d|30|31")
# months = re.compile(r"/(0[1-9])/|/(1[0-2])/")
# years = re.compile(r"[1-2][0-9][0-9][0-9]")
# day = days.search(data[:2])
# month = months.search(data[2:6])
# year = years.search(data[6:])
# day = int(day.group())
# month = int(int(month.group()[1:3]))
# year = year.group()
# print(day)
# print(month)
# print(year) 


month = months_finder(date)
day = days_finder(date, month)
month = months_finder(date)
year = years_finder(date)

print(day)
print(month)
print(year) 



# def day_check(data2day):
#     if str(data_day).startswith("0"):
#         if data_day[1] == 0:
#             return False
#         return True
#     else:
#         if int(data_day)<=31:
#             return True
#         return False
    

# print(day_check(data_day))
