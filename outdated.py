def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]


    while True:

        try:

            date = str(input("Date: "))

            monthstr, daystr, year = date.split(" ")

            month = months.index(monthstr.strip()) + 1
            daystrip = daystr.rstrip(",")
            dayint = int(daystrip)
            yearpt = year.strip()

            if month <=12 and dayint <= 31 and not daystr.isnumeric():

                print (yearpt, end = "-")
                print (f"{month:02}", end = "-")
                print (f"{dayint:02}")
                break

            else:

                pass

        except ValueError:

            try:

                month1, day1, year1, = date.split("/")

                month2 = int(month1)

                day2 = int(day1)

                yeartopt = year1.strip()

                if month2 <= 12 and day2 <= 31:

                    print (yeartopt, end = "-")

                    print (f"{month2:02}", end = "-")

                    print (f"{day2:02}")

                    break

                else:

                    pass

            except ValueError:
                pass
        pass

main()