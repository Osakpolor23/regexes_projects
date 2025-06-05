import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Use regex to match the IPv4 address format
    matches = re.search(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ip, re.IGNORECASE)
    # Check if the matches were found
    if matches:
        # map the matched string to a list of octets by splitting at the dots
        octets = matches.group().split(".")
        # Check if each octet is within the range of 0 to 255
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                # if any octet is not in the range, return False
                return False
        # If all octets are valid, return True
        return True
    # If no matches were found, return False
    else:
        return False

# Call the main function only when run in the terminal
if __name__ == "__main__":
    main()