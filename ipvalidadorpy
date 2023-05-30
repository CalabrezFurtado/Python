import re
import sys

'''validates IP - has some flaws''' 
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    return bool(re.search (r"^((([0-2]?[0-5]?[0-5])|([0-2]?[0-4]?[0-9])|([0-1]?[0-9]?[0-9]))(\.|$)){4}", ip))

if __name__ == "__main__":
    main()
