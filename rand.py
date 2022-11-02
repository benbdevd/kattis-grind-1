#!/usr/bin/env python3
import os
import sys
import random
import argparse


def get_problem_difficulty(problem):
    tds = problem.find_all('td')
    text = tds[6].text.split('.')
    return float(text[0] + '.' + text[1][:1])


try:
    import requests
except ImportError:
    sys.exit("You need requests. run 'pip install requests'")

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("You need BeautifulSoup. run 'pip install bs4'")

try:
    from fake_useragent import UserAgent
except ImportError:
    sys.exit("You need UserAgent. run 'pip install fake-useragent'")

parser = argparse.ArgumentParser(description='Runs Kattis problem through their test cases')
parser.add_argument('-n', type=int, default=None, help='the amount of problems wanted to fetch')
parser.add_argument('-l', type=float, default=None, help='the lower bound for problems')
parser.add_argument('-u', type=float, default=None, help='the upper bound for problems')

args = parser.parse_args()
n= args.n
lower_bound = args.l
upper_bound = args.u

if n is None:
    n = int(input('How many problems: '))

if lower_bound is None:
    lower_bound = float(input('Enter lower bound: '))

if upper_bound is None:
    upper_bound = float(input('Enter upper bound: '))

tmp = upper_bound
upper_bound = min(max(upper_bound, lower_bound), 10)
lower_bound = max(min(lower_bound, tmp), 0)

seenlist = []
if os.path.isfile('./seen.txt'):
    seenlist = [line.rstrip('\n') for line in open('./seen.txt')]

qlist = []
done = False
i = 0
while not done:
    url = 'https://open.kattis.com/problems?page=' + str(i) + '&order=problem_difficulty'
    usa = UserAgent()
    page = requests.get(url, headers={'User-Agent':str(usa.random)})
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table', attrs={'class': 'table2'})

    if table is None:
        done = True

    tbody = table.find('tbody')
    problems = tbody.find_all('tr')

    if problems:
        greatest_diff = get_problem_difficulty(problems[-1])

        if greatest_diff < lower_bound:
            i += 1
            continue

    for problem in problems:
        tds = problem.find_all('td')

        try:
            diff = get_problem_difficulty(problem)
        except ValueError:
            continue

        if diff > upper_bound:
            done = True

        elif diff >= lower_bound and diff <= upper_bound:
            qid_url = tds[0].find('a')['href']
            if qid_url.split('/')[2] not in seenlist:
                qlist.append(qid_url.split('/')[2])
    i += 1

random.shuffle(qlist)
qlist = qlist[:n]

print(f'Here are {n} Kattis problems: {qlist}')

for qid in qlist:
    os.popen('python3 ./fetch.py ' + qid)

print('The problems have been scraped and saved')
