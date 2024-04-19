import datetime
import math

def calculate_jd(year, month, day, hour , minute , second ,  ut):

# Perform the calculation
    julian_datetime = 367 * year - int((7 * (year + int((month + 9) / 12.0))) / 4.0) + int(
        (275 * month) / 9.0) + day + 1721013.5 + (hour + minute / 60.0 + second / math.pow(60,2)) / 24.0 - 0.5 * math.copysign(1, 100 * year + month - 190002.5) + 0.5

    return julian_datetime

def calculate_lst(jd, longitude, ut):
    GMST = 18.697374558 + 24.06570982441908 * (jd - 2451545)
    LST = GMST + longitude / 15 + ut
    LST %= 24
    return LST

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day of the month: "))
    hour = int(input("Enter hour (0-23): "))
    minute = int(input("Enter minute (0-59): "))
    second = int(input("Enter second (0-59): "))
    location_input = input("Enter latitude and longitude of your location separated by comma (e.g., 23.817043,86.441662): ")
    latitude, longitude = map(float, location_input.split(','))
    
    standard_time = datetime.datetime(year, month, day, hour, minute, second)
    ut = standard_time.hour + standard_time.minute / 60 + standard_time.second / 3600
    
    jd = calculate_jd(year, month, day, hour , minute , second ,  ut)
    lst = calculate_lst(jd, longitude, ut)
    
    print("Standard Time:", standard_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Julian Day:", jd)
    print("Local Sidereal Time (LST):", lst)
    print(" ") 
    print("code by Sonu Kumar 20JE0961 and Suyash Suryavanshi 20JE1005")

if __name__ == "__main__":
    main()
