import requests
import hashlib
site = "http://youtube.com"
initial_hash = ""


def get_hash():
    rep = requests.get(site)
    bytes = rep.text.encode("utf-8")
    return hashlib.md5(bytes).hexdigest()


def set_initial_hash():
    # i know i shouldn't use globals
    global initial_hash
    if initial_hash:
        print("This shouldn't be called with an existing hash")
        return False
    initial_hash = get_hash()


if __name__ == "__main__":
    set_initial_hash()
    print(initial_hash)
