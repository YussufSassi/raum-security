from time import sleep
import sys
from mfrc522 import SimpleMFRC522

r = SimpleMFRC522()


def read_card(reader: SimpleMFRC522):
    id, text = reader.read()
    return id, text


if __name__ == "__main__":
    while True:
        print(read_card(r))
        sleep(2)
