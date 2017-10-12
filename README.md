# Page Checker

## What is this?
It's a Discord bot that I made in an afternoon. It scrapes web pages and sends a message if they've changed.
## Should I use it?
No. Because I built it so quickly, it's not very good. I might later make it better, and properly packaged, and all that. (But I probably won't)
## I really want to though.
You shouldn't.

1. Set up your Discord bot account & get the token & add it to your server & all that. (You probably know how to do this better than I do.)
2. Install dependancies. Aside from a recent-ish version of Python 3, everything else comes from `requirements.txt` (`pip3 install -r requirements.txt`)
3. Make a `config.py` file that looks a bit like this:
```python
very_secret_key = "[The bot's token]"
site = "https://[The site you want checked]"
server_id = "[The ID of the server you want to run the bot in]"
channel_id = "[The ID of the channel you want to run the bot in]"
time_between_tries = [Time in minutes between each scrape of the page
```
4. Run `main.py`.
5. I warned you.

## Known Issues
On some `https` urls, it fails. I think this is caused by the async http library I'm using not handling certificates properly.
To fix this, use `http` urls instead.
