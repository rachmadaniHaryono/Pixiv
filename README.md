# Pixiv Downloader
---

A simple tool to download all illustrations from specific illustrator.

Download illustrations by **user's id**, **daily ranking** or **history ranking**.

---

## Features
- [x] Keep login sessions
  - [x] Local storage
  - [x] Secure storage (not memory safe)
- [x] Update downloaded artists
- [x] Refresh downloaded artists
- [x] Multi-Language
- [x] CLI Interface

## Requirement

[Requests](http://docs.python-requests.org/)

[PyCrypto](https://www.dlitz.net/software/pycrypto/)


## Screenshot

pixiv.py

![img](https://raw.github.com/bebound/Pixiv/master/ScreenShot/4.png)


## CLI Usage

    usage: Pixiv.py [-h] [--download-by-user-id user-id] [--download-by-ranking]
                [--download-by-history-ranking] [--update-exist]
                [--refresh-exist] [--remove-repeat]

optional arguments:

    -h, --help            show this help message and exit
    --download-by-user-id user-id
                          Download by user id.
    --download-by-ranking
                          Download by ranking.
    --download-by-history-ranking
                          Download by history ranking.
    --update-exist        Update existing collections.
    --refresh-exist       Refresh existing collections.
    --remove-repeat       Remove duplicate in collections.

## Credits
- [Pixiv-API](https://github.com/twopon/Pixiv-API)
- [PixivPy](https://github.com/upbit/pixivpy)
- [pixiv api](https://danbooru.donmai.us/wiki_pages/58938)
