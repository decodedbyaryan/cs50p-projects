import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    user_input = re.fullmatch(r"(\d+)(:\d+)? (AM|PM) to (\d+)(:\d+)? (AM|PM)", s)

    if user_input:
        hour_start = int(user_input.group(1))
        min_start = user_input.group(2)
        ampm_start = user_input.group(3)
        hour_end = int(user_input.group(4))
        min_end = user_input.group(5)
        ampm_end = user_input.group(6)

        if min_start:
            min_start = int(min_start[1:])
        else:
            min_start = 0

        if min_end:
            min_end = int(min_end[1:])

        else:
            min_end = 0

        if hour_start > 12 or hour_start < 1:
            raise ValueError
        
        if hour_end > 12 or hour_end < 1:
            raise ValueError
        
        if min_start > 59 or min_start < 0:
            raise ValueError
        
        if min_end > 59 or min_end < 0:
            raise ValueError

        if hour_start:
            if ampm_start == "AM" and hour_start == 12:
                hour_start = 00
            elif ampm_start == "PM" and hour_start != 12:
                hour_start += 12
            else:
                hour_start = hour_start

        if hour_end:
            if ampm_end == "AM" and hour_end == 12:
                hour_end = 00
            elif ampm_end == "PM" and hour_end != 12:
                hour_end += 12
            else:
                hour_end = hour_end

        return(f"{hour_start:02d}:{min_start:02d} to {hour_end:02d}:{min_end:02d}") 

    else:
        raise ValueError
    
if __name__ == "__main__":
    main()