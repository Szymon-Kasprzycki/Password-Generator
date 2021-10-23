# Password Generator
# Author: Szymon Kasprzycki
# v1.0.0
# Made for educational purpose

import string
import random


def generate(length: int = 16, allowedChars: str = None):
    alphabet = string.ascii_lowercase + string.digits
    if allowedChars:
        alphabet += allowedChars
    password = "".join(random.choices(alphabet, k=length))
    return password


def save(filename: str, password: str):
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        f.write(password)
    return


if __name__ == "__main__":
    len = input(
        "Tell me the length of the password (leave blank if don't know) --> "
    ).strip()
    allowedChars = input(
        "Tell me the special characters you want to be used in password eg. *&$@#?. --> "
    ).strip()
    if len:
        try:
            len = int(len)
        except Exception as e:
            print("This length is not allowed!")
    passwd = generate(len, allowedChars)
    save("passwd", passwd)
    print(
        "Your password was successfully generated, you can find it in 'passwd.txt' file in script's root directory."
    )
