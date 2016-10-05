# Hacker Buzz Utils #

## Docker and Docker Compose ##

* Assuming you are using docker and docker-compose, to the the container running do:

```
$ git clone https://github.com/lcdporto/hacker-buzz-utils.git
$ cd hacker-buzz-utils
$ docker-compose up -d
```

* Now that you have the container runnning you can:

```
# scissors.txt is text file with one image url per line
# from outside the container use full paths
$ docker exec -ti hacker-buzz-utils python3 /app/scripts/download.py -f /app/scripts/scissors.txt -d /app/images/scissors
```

* Or you can also do:

```
# scissors.txt is text file with one image url per line
$ docker exec -ti hacker-buzz-utils bash
$ cd /app/scripts

# to get help
$ python3 download.py --help

# to download from an url
$ python3 download.py <url>

# to download from a file containing one url per line
$ python3 download.py -f scissors.txt
```
