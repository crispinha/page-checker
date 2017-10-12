import requests
import hashlib
site = "http://youtube.com"


def get_hash():
    rep = requests.get(site)
    bytes = rep.text.encode("utf-8")
    print(hashlib.md5(bytes).hexdigest())


if __name__ == "__main__":
    get_hash()
