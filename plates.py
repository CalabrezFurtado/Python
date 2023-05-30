'''checks validity of Vanity Plates according to their standards''' 

def main():

 test_plates.test_plates.py   global plate
    plate= str(input("Plate: ")).strip()

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):


    if content(plate) == False:
        return False

    elif firstnumis0(plate) == False:
        return False

    elif len(s)>6 or len(s)<2:
        return False

    elif  not s[0:2].isalpha():
        return False

    elif len(s)==4:

        if s[2:3].isnumeric() and s[3:4].isalpha():
            return False

        else:
            return True

    elif len(s)==5:

        if s[4:5].isalpha() and s[2:3].isnumeric() or s[4:5].isalpha() and s[3:4].isnumeric():
            return False

        elif s[3:4].isalpha() and s[2:3].isnumeric():
            return False

        else:
            return True

    elif len(s)==6:

        if s[5:6].isalpha() and s[2:3].isnumeric() or s[5:6].isalpha() and s[3:4].isnumeric() or s[5:6].isalpha() and s[4:5].isnumeric():
            return False

        elif s[4:5].isalpha() and s[2:3].isnumeric() or s[4:5].isalpha() and s[3:4].isnumeric():
            return False

        elif s[3:4].isalpha() and s[2:3].isnumeric():
            return False

        else:
            return True


def content(plate):



    for unit in plate:

               if not unit.isalpha() and not unit.isnumeric():
                    return False


def firstnumis0(plate):

    for i in range (0, len(plate)):
        if plate[i].isalpha() == False:
            if plate[i] == "0":

                return False
            else:
                break



main()
