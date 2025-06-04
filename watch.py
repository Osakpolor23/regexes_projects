import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # match the embedded url pattern in the argument parsed, using regex 
    matches = re.search(r'(?:<iframe)? src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9?=_-]+)(?:></iframe>)?"',s, re.IGNORECASE)

    # check if matches were found
    if matches:
        # extract just the last part of the value of the embedded src attribute
        video_id = matches.group(1)
        # then return the shortened youtu.be link
        return f"https://youtu.be/{video_id}"
    # if no match
    else:
        # return None
        return None

# call the main function only when run in the terminal
if __name__ == "__main__":
    main()