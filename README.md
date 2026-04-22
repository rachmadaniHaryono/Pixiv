# PixivD

[![PyPI version](https://badge.fury.io/py/pixivd.svg)](https://badge.fury.io/py/pixivd)

A simple tool to download illustrations from Pixiv.

Download illustrations by **uers\_id**, **daily ranking** or **history ranking**.

## Features

- [x] Keep login sessions
    - [x] Local storage
    - [x] Secure storage (not memory safe)
- [x] Update downloaded artists
- [x] Refresh downloaded artists
- [x] Mutil-Language
- [x] Command-line interface
- [x] Docker image

## Installation

`pip install pixivd`

Or you can use it with `uv`'s `uvx pixivd`

### Docker

Setting `PIXIVD_AES_INT` to a fixed integer to persist the login sessions.

`docker run -v ./:/app -e PIXIVD_AES_INT=123 --rm -it ghcr.io/bebound/pixivd`

## Usage

```
    pixivd
    pixivd <id>...
    pixivd -r [-d | --date=<date>]
    pixivd -u

Arguments:
    <id>                                       user_ids

Options:
    -r                                         Download by ranking
    -d <date> --date <date>                    Target date
    -u                                         Update exist folder
    -h --help                                  Show this screen
    -v --version                               Show version

Examples:
    pixivd 7210261 1980643
    pixivd -r -d 2016-09-24
```

The illusts will be downloaded to `illustrations` folder in current directory.

## Screenshot

![img](https://raw.github.com/bebound/Pixiv/master/ScreenShot/3.0.png)

## Credits

- [Pixiv-API](https://github.com/twopon/Pixiv-API)
- [PixivPy](https://github.com/upbit/pixivpy)
- [pixiv api](https://danbooru.donmai.us/wiki_pages/58938)
- [Pixiv OAuth Flow](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362)

