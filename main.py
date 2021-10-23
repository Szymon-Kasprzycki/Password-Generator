# Password Generator
# Author: Szymon Kasprzycki
# v1.0.0
# Made for educational purpose

import string
import random


def generate(length: int = 16, allowedChars: str = None, UpperCase: bool = False):
    alphabet = string.ascii_lowercase + string.digits
    if allowedChars:
        alphabet += allowedChars
    if UpperCase:
        alphabet += string.ascii_uppercase
    password = "".join(random.choices(alphabet, k=length))
    return password


def save(filename: str, password: str):
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(password)
    return


def main():
    len = input(
        "Tell me the length of the password (leave blank if don't know) --> "
    ).strip()
    allowedChars = input(
        "Tell me the special characters you want to be used in password eg. *&$@#?. --> "
    ).strip()
    upperCase = (
        input("Do you want uppercase letters in your password? (y/n) --> ")
        .strip()
        .lower()
    )
    if upperCase == "y":
        upperCase = True
    elif upperCase == "n":
        upperCase = False
    else:
        upperCase = None
        print("Please type in correct values in uppercase letters question!")
        return

    if len:
        try:
            len = int(len)
        except Exception:
            print("This length is not allowed!")
            return
    passwd = generate(len, allowedChars, upperCase)
    try:
        save("passwd", passwd)
    except PermissionError:
        print("Couldn't save file with password. Don't have enough permissions!")
    except Exception as e:
        print(f"Error: {e}")
    print(
        "Your password was successfully generated, you can find it in 'passwd.txt' file in script's root directory."
    )


if __name__ == "__main__":
    main()
