"""Download the lab's fixed archive snapshot into the current folder."""

from urllib.request import urlretrieve
from zipfile import ZipFile

for year in range(2009, 2019):
    filename = f'master_{year}.json.zip'
    url = ('https://raw.githubusercontent.com/bpb27/trump_tweet_data_archive/'
           '4b156c24e44815a12da839641bb6c18542345f10/')
    print('Downloading', filename)
    urlretrieve(url + filename, filename)
    with ZipFile(filename) as archive:
        archive.extractall('.')
