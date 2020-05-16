# -*- conding: utf-8 -*-
"""
@author by mkzhou
@time 2020/5/16 10:04
图书排名
"""

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen

REGEX = compile(b'#([\d,]+) in Books ')
AMZN = 'http://amazon.com.cn/dp/'
ISBNS = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals'
}

def getRanking(isbn):
    page = urlopen('{}{}'.format(AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    # print('-{} ranked {}'.format(ISBNS[isbn], getRanking(isbn)))
    Thread(target=_showRanking, args=(isbn, )).start()

def _main():
    print('At {} on Amazon...'.format(ctime()))
    for isbn in ISBNS:
        _showRanking(isbn)

@register
def _atexit():
    print('all done at {}'.format(ctime()))

if __name__ == "__main__":
    _main()