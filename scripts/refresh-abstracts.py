#!/usr/bin/env python3
"""Manually refresh the site's saved arXiv abstracts."""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
ATOM = '{http://www.w3.org/2005/Atom}'


def validate_feed(xml):
    feed = ET.fromstring(xml)
    if feed.tag != ATOM + 'feed':
        raise ValueError('Expected an Atom feed')
    entries = feed.findall(ATOM + 'entry')
    if any('/api/errors' in entry.findtext(ATOM + 'id', '') for entry in entries):
        raise ValueError('arXiv returned an API error')
    if not entries or any(not entry.findtext(ATOM + 'summary', '').strip() for entry in entries):
        raise ValueError('Refusing to replace a snapshot with missing abstracts')
    return len(entries)


def main():
    query = urlencode({'search_query': 'au:"Kunal Marwaha"', 'max_results': 200})
    request = Request('https://export.arxiv.org/api/query?' + query,
                      headers={'User-Agent': 'arxiv-wordcloud (https://github.com/marwahaha/arxiv-wordcloud)'})
    with urlopen(request, timeout=60) as response:
        xml = response.read()
    count = validate_feed(xml)
    target = ROOT / 'feeds/kunal-marwaha.xml'
    temporary = target.with_suffix('.tmp')
    temporary.write_bytes(xml)
    temporary.replace(target)
    print('Saved ' + str(count) + ' arXiv abstracts for Kunal Marwaha')


if __name__ == '__main__':
    main()
