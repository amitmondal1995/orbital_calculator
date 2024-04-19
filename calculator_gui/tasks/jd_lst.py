"""
This module calculates the Julian Date based on the provided year, month, and day.
"""

def calculate_julian_date(year, month, day):
    """
    Calculate the Julian Date based on the provided year, month, and day.

    Parameters:
    - year: Year
    - month: Month (1-12)
    - day: Day of the month

    Returns:
    - Julian Date
    """
    # Perform the calculation
    term1 = 367 * year - (7 * (year + (month + 9) // 12)) // 4
    term2 = (275 * month) // 9 + day + 1721013.5
    julian_datetime =  term1 + term2

    return julian_datetime

def calculate_lst(julian_date, longitude, utc_time):
    """
    Calculate Local Sidereal Time (LST) based on the provided Julian Date, longitude, and UTC time.

    Parameters:
    - julian_date: Julian Date
    - longitude: Longitude of the location (in degrees)
    - utc_time: Universal Time (in hours)

    Returns:
    - Local Sidereal Time (in hours)
    """
    gmst = 18.697374558 + 24.06570982441908 * (julian_date - 2451545)
    lst = gmst + longitude / 15 + utc_time
    lst %= 24
    return lst

# def main():
#     """
#     taking inputs like year,month ,  date
#     """
#     year = int(input("Enter year: "))
#     month = int(input("Enter month (1-12): "))
#     day = int(input("Enter day of the month: "))
#     hour = int(input("Enter hour (0-23): "))
#     minute = int(input("Enter minute (0-59): "))
#     second = int(input("Enter second (0-59): "))
#     longitude = float(input("Enter the longitude of your location (e.g., 86.441662): "))

#     standard_time = datetime.datetime(year, month, day, hour, minute, second)
#     utc_time = standard_time.hour + standard_time.minute / 60 + standard_time.second / 3600
#     julian_date = calculate_julian_date(year, month, day)
#     lst = calculate_lst(julian_date, longitude, utc_time)
#     print("Standard Time:", standard_time.strftime("%Y-%m-%d %H:%M:%S"))
#     print("Julian Day:", julian_date)
#     print("Local Sidereal Time (LST):", lst)
#     print(" ")
#     print("Code by Sonu Kumar (20JE0961) and Suyash Suryavanshi (20JE1005)")

# if __name__ == "__main__":
#     main()
