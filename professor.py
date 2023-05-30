import random

def main():

    le = get_level()
    score = int()

    for trials in range (10):

        try:

                generate_integer(le)
                equation = x + y
                sum = int(input(f"{x} + {y} = "))
                if sum == equation:
                    score += 1

                elif sum != equation:
                    raise ValueError


        except ValueError:
            print ("EEE")
            try:

                sum2 = int(input(f"{x} + {y} = "))

                if sum2 == equation:
                    score += 1

                elif sum2 != equation:
                    raise ValueError

            except ValueError:
                print("EEE")
                try:
                    sum3 = int(input(f"{x} + {y} = "))
                    if sum3 == equation:
                        score += 1

                    elif sum3 != equation:
                        raise ValueError

                except ValueError:
                    print("EEE")
                    print (f"{x}+{y}={equation}")
                    pass

    print (f"Score = {score}")

def get_level():

    while True:
        try:


            lev = int(input("Level: "))

            if lev == 1 or lev == 2 or lev == 3:

                return lev

            else:
                pass

        except ValueError:
            pass
        return lev

def generate_integer(lev):
    global x
    global y
    if lev == 1:

        x = random.randint(0,9)

        y = random.randint(0,9)
        return x, y

    elif lev == 2:


        x = random.randint(10,99)

        y = random.randint(10,99)
        return x, y

    elif lev == 3:


        x = random.randint(100,999)

        y = random.randint(100,999)
        return x, y
    return x,y


if __name__ == "__main__":
    main()