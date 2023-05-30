import re
import sys

'''converts AM-PM time to 0-24hr'''
def main():

    print(convert(input("Hours: ")))


def convert(s):

    s1,s2 = s.split(' to ')
    groups1 = re.findall (r'(?:(?:(^(?:[1][0-2])|(?:[1-9]))(?::([0-5][0-9]))? (AM))|(^(?:[1][0-2])|(?:[1-9]))(?::([0-5][0-9]))? (PM))(?: to )(?:(?:((?:[1][0-2])|(?:[1-9]))(?::([0-5][0-9]))? (AM))|((?:[1][0-2])|(?:[1-9]))(?::([0-5][0-9]))? (PM))', s)

    if groups1 == []:
        raise ValueError

    else:

        groups = list(groups1[0])


        if ':' not in s1:

            groups.pop(1)
            groups.insert(1,'00')
            groups.pop(4)
            groups.insert(4,'00')

        if ':' not in s2:

            groups.pop(7)
            groups.insert(7,'00')
            groups.pop(10)
            groups.insert(10,'00')

        if 'AM' in s1 and groups[0] == '12':

            groups.pop(0)
            groups.insert(0,'00')

        if 'AM' in s2 and groups[6] == '12':

            groups.pop(6)
            groups.insert(6,'00')

        if 'AM' in s1 and int(groups[0]) < 10 and int(groups[0]) != 0:

            groups[0]
            hour = '0' + groups[0]
            groups.pop(0)
            groups.insert(0,hour)

        if 'AM' in s2 and int(groups[6]) < 10 and int(groups[6]) != 0:

            groups[6]
            hour = '0' + groups[6]
            groups.pop(6)
            groups.insert(6,hour)

        if 'PM' in s1 and int(groups[3]) < 10 and int(groups[3]) != 0:

            groups[3]
            hour = '0' + groups[3]
            groups.pop(3)
            groups.insert(3,hour)

        if 'PM' in s2 and int(groups[9]) < 10 and int(groups[9]) != 00  :

            groups[9]
            hour = '0' + groups[9]
            groups.pop(9)
            groups.insert(9,hour)

        if 'AM' in s1 and 'AM' in s2:

                newstringAMAM1 = groups[0] + ':' + groups[1] + ' to ' + groups[6] + ':' + groups[7]
                return newstringAMAM1

        elif 'AM' in s1 and 'PM' in s2:

                if int(groups[9]) == 12:

                    newstringAMPM = groups[0] + ':' + groups[1] + ' to ' + groups[9] + ':' + groups[10]
                    return newstringAMPM

                else:

                    pmhour2 = int(groups[9]) + 12

                    newstringAMPM1 = groups[0] +  ':' + groups[1]+ ' to ' + str(pmhour2)+ ':' +groups[10]
                    return newstringAMPM1

        elif 'PM' in s1 and 'PM' in s2:

                if int(groups[3])==12 and int(groups[9])==12:

                    newstringPMAM1 = groups[3]+ ':' + groups[4] + ' to ' + groups[9] + groups[10]
                    return newstringPMAM1

                elif int(groups[3])==12:

                    pmhour2 = int(groups[9]) + 12
                    newstringPMPM = groups[3] + ':' + groups[4] + ' to ' +  str(pmhour2) + ':' + groups[10]
                    return newstringPMPM

                elif int(groups[9])==12:

                    pmhour = int(groups[3]) + 12
                    newstringPMPM = str(pmhour) + ':' + groups[4] + ' to ' +  groups[9] + ':' + groups[10]
                    return newstringPMPM

                else:

                    pmhour = int(groups[3]) + 12
                    pmhour2 = int(groups[9]) + 12
                    newstringPMPM = str(pmhour) + ':' + groups[4] + ' to ' +  str(pmhour2) + ':' + groups[10]
                    return newstringPMPM

        elif 'PM' in s1 and 'AM' in s2:


                if int(groups[3])==12:

                    newstringPMAM1 = groups[3] + ':' + groups[4] + ' to ' + groups[6] + ':' + groups[7]
                    return newstringPMAM1

                else:
                    pmhour = int(groups[3]) + 12
                    newstringPMAM2 = str(pmhour) + ':' + groups[4] + ' to ' + groups[6] + ':' + groups[7]
                    return newstringPMAM2



if __name__ == "__main__":
    main()
