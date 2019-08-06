from locust import HttpLocust, TaskSet, task, stats
import csv

INPUT_FILE = 'log.tsv'

queue = []
with open(INPUT_FILE, newline='') as tsvfile:
    lines = csv.reader(tsvfile, delimiter="\t")
    next(lines) # skip header row
    for line in lines:
        queue.append( line[2] )

class MyTaskSet(TaskSet):
    @task(1)
    def solrQuery(self):
        if len(queue) > 0:
            self.client.get(queue.pop(), name="Solr Query")

class WebsiteUser(HttpLocust):
    # meaningless, because we're using full URLs, but require by Locust
    host = "https://www.hathitrust.org/"
    task_set = MyTaskSet
    min_wait = 10000
    max_wait = 10000

