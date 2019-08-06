# solr-load-testing-experiments
## locust
Use locust to fetch a supplied list of URLs. Probably get stuck in a dry loop once we run out of URLs. Doesn't work great as locust expects to fetch few URL many times, not many URLs once.

### setup
* [install locust](https://docs.locust.io/en/stable/installation.html)
* put log.tsv in the same dir, or edit locustfile.py to include the correct pathname.

### run
10 second wait (set in locustfile.py), 20 locusts and spawn rate of 1 (set in GUI or on command line as show below) levels out right at 2 RPS.

* q/ GUI: `locust`
* w/o GUI: `locust --no-web -c 20 -r 1`
