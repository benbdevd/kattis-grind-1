#!/usr/bin/env python3
import os
import sys
import shutil
import pathlib
import requests
import argparse

try:
    import requests
except ImportError:
    sys.exit("You need requests. run 'pip install requests'")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("You need BeautifulSoup. run 'pip install beautifulsoup4'")

try:
    from fake_useragent import UserAgent
except ImportError:
    sys.exit("You need UserAgent. run 'pip install fake-useragent'")

parser = argparse.ArgumentParser(description='Fetches random Kattis Problems')
parser.add_argument('qid', metavar='ID', type=str, help='id of problem to fetch')
args = parser.parse_args()
qid = args.qid

if qid == None:
    qid = input('Enter ID: ')

PROBLEMS_PATH = './problems/'
PROBLEM_PATH = PROBLEMS_PATH + qid

if os.path.isdir(PROBLEM_PATH + qid):
    print('This problem already exists.')
    exit(1)
pathlib.Path(PROBLEM_PATH).mkdir(parents=True, exist_ok=True)

url = 'http://open.kattis.com/problems/' + qid
usa = UserAgent()

page = requests.get(url, headers={'User-Agent':str(usa.random)})
soup = BeautifulSoup(page.content, 'html.parser')

tableinp = soup.find_all('table', attrs={'class': 'sample'})

htmlfile = soup
for section in htmlfile.find_all('section', {'class': 'box clearfix main-content problem-sidebar'}): section.decompose()
for div in htmlfile.find_all('div', {'class':['wrap', 'description','footer','problem-download','footer-powered col-md-8']}): div.decompose()
for img in htmlfile.find_all('img'): img.decompose()
for a in htmlfile.find_all('a'): a.decompose()

pathlib.Path(PROBLEM_PATH + '/' + qid + '.html').write_text(str(htmlfile))

i = 0
for sample in tableinp:
    tablestd = sample.find_all('pre')
    pathlib.Path(PROBLEM_PATH + '/input' + str(i + 1)).write_text(tablestd[0].text)
    pathlib.Path(PROBLEM_PATH + '/output' + str(i + 1)).write_text(tablestd[1].text)
    i += 1

src = os.curdir
dst = os.path.join(src, PROBLEM_PATH)
cpp = os.path.join(src, 'template.cpp')

shutil.copy(cpp, dst)

dstfile = os.path.join(dst,'template.cpp')
newfile = os.path.join(dst,'_' + qid + '.cpp')
os.rename(dstfile, newfile)

python_file_path = (PROBLEM_PATH + '/_' + qid + '.py')

with open(python_file_path, 'w+') as python_file:
    python_file.write('#!/usr/bin/env python3\n')
    os.chmod(python_file_path, 0o777)

if not os.path.isfile('./seen.txt'):
    open('seen.txt', 'w+')

with open('seen.txt','a') as f:
    f.write(qid + '\n')
