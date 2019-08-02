# solr-load-testing-experiments
## locust
Use locust to fetch a supplied list of URLs. Probably get stuck in a dry loop once we run out of URLs. Doesn't work great as locust expects to fetch few URL many times, not many URLs once.
### setup
* [install locust](https://docs.locust.io/en/stable/installation.html)
* put log.tsv in the same dir, or edit locustfile.py to include the correct pathname.
### run
`locust`
