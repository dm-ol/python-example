# pip install httpx
# Цікавий пакет для роботи із веб-запитами. Як кажуть самі розробники, це HTTP-клієнт наступного покоління.
# https://www.python-httpx.org/

import httpx
r = httpx.get('https://www.example.org/')
r
Response[200 0K] >
r.status_code
200
r.headers['content-type']
'text/html; charset=UTF-8'
r.text
'<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>...'
