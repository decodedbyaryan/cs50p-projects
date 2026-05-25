def main():
    

    

    while True:

        try:
            date = input("date in MM/DD/YYYY or month day, year format: ")

            months = ["January", "February", "March", "April", "May", "June", "July",
                      "August", "September", "October", "November", "December"]


            if "," in date:
                parts = date.split(", ")
                month_day = parts[0].split(" ")
                month_name = month_day[0]
                dd = int(month_day[1])
                yy = int(parts[1])
                if month_name not in months:
                    continue
                mm = months.index(month_name) + 1

            else:

                parts = date.split("/")
                mm = int(parts[0])
                dd = int(parts[1])
                yy = int(parts[2])
        
                if mm < 1 or mm > 12 or dd > 31 or dd < 1:
                    continue


            print(f"{yy}-{mm:02}-{dd:02}")
            break

        except ValueError:
            continue




main()