import re
import sys

# The program takes working hours e.g 9 am to 5pm and converts to a 24hr time e.g 09:00 to 17:00

def main():
    hours = input("Hours: ")
    print(convert(hours))


def convert(hours):
    # get the exact matches for the hour, minute and period
    matches = re.search(r"^(\d{1,2}):?(\d{2})?\s?(AM|PM)\s(?:to)\s(\d{1,2}):?(\d{2})?\s?(AM|PM)?$", hours, re.IGNORECASE)
    
    # check for where matches are not found
    if not matches:
        raise ValueError("Invalid time format")
    
    # if matched, extract the minute
    if matches:
            # extract the minutes groups and default to "00" if None
            minutes_start  = matches.group(2) if matches.group(2) is not None else "00" # return 00 if minutes were not provided
            minutes_end = matches.group(5) if matches.group(5) is not None else "00" # return 00 if minutes were not provided

    # Ensure minutes are within the range of 0 and 59
    if not (0 <= int(minutes_start) <= 59 and 0 <= int(minutes_end) <= 59):
        raise ValueError("Invalid minute format")
    
    # Convert AM/PM periods to uppercase to handle lowercase inputs
    period_start = matches.group(3).upper() 
    period_end = matches.group(6).upper() if matches.group(6) is not None else ""  # for eventualities like 9am to 17:00


    # Convert hours to 24-hour format
    hours_start = convert_hour(matches.group(1), period_start)  # using the convert_hour(hour, period) function
    hours_end = convert_hour(matches.group(4), period_end)
    
    # return the converted 
    return (f"{hours_start}:{minutes_start} to {hours_end}:{minutes_end}")

# create a helper function to convert 12hrs format to 24hrs format
def convert_hour(hours, period):
    # use the extracted values to get do the conversion
    if hours == "12" and period == "AM":
        return '00'  # for midnight
    elif period == "PM" and hours != "12":
        return str(int(hours) + 12)  # convert to 24hr format by adding 12
    else:
        return hours.zfill(2) # Ensuring leading zeros for AM hours (zfill() is used because it is strings)
                                # n:02 only work for digits


if __name__ == "__main__":
    main()