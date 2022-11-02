# Kattis Grind
A small easy-to-use package of Python 3 scripts which can help speed up the process for competitive programming on [Kattis](https://open.kattis.com). The scripts will download a local copy of the question (html file), and can automate testing inputs and outputs.

# Requirements
Kattis Grind uses Python 3. To check if you have it:
```console
foo@bar:~$ python3 --version
Python 3.7.3
```

If you don't have Python 3, you can install it from the [Python Website](https://www.python.org/downloads/).

The Kattis Grind setup requires requests, beautifulsoup4, and fake-useragent. To install them, execute
```console
foo@bar:~$ pip3 install -r requirements.txt
```

# How do I use it?
## Fetch a Question!
```console
foo@bar:~/kattis-grind$ ./fetch.py hello
```

## Test Your Solution!
```console
foo@bar:~/kattis-grind$ ./test.py hello
```

## Fetch Random Questions!
```console
foo@bar:~/kattis-grind$ ./rand.py
How many problems: 5
Enter lower bound: 1.4
Enter upper bound: 1.6
```

There are optional command line arguments
```console
foo@bar:~/kattis-grind$ ./rand.py -n 5 -l 1.4 -u 1.6
```

Depending on how many questions you want, and what range they're between, this operation *may* take several seconds (sometimes a good 10 - 40 seconds!!). Keep in mind that while it takes long, it definitely works!

# Current Bugs
Currently, Windows seems to have some trouble with encoding characters and Python crashes as a result of trying to save HTML files without proper encoding. This does not occur on Linux. Be wary of questions with foreign characters in them, for example: ő

# License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

# Acknowledgments
* Thanks to [JarateKing](https://github.com/JarateKing) and [Ben Boyle](https://github.com/benbdevd) for the original grinding idea.
* Thanks to [Will Taylor](https://github.com/wtaylor17) for fixing test.py to work on Windows machines.
* Thanks to the UPEI SMCSS for all the motivation!!!
