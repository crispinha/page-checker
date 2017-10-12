import aiohttp
import hashlib
import config
site = config.site
initial_hash = ""


async def get_hash():
    async with aiohttp.get(site) as rep:
        text = await rep.text()
        bytes = text.encode("utf-8")
        return hashlib.md5(bytes).hexdigest()


async def set_initial_hash():
    # i know i shouldn't use globals
    global initial_hash
    if initial_hash:
        print("This shouldn't be called with an existing hash")
        return False
    initial_hash = await get_hash()


async def has_hash_changed():
    new_hash = await get_hash()
    if new_hash == initial_hash:
        return False
    else:
        initial_hash == new_hash
        return True
