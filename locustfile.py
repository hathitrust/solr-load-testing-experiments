from locust import HttpLocust, TaskSet, task, stats
import csv

INPUT_FILE = 'log.tsv'

def monkey_get(self, _, method):
    """
    Retrieve a StatsEntry instance by method, ignore name
    """
    name = "URL"
    entry = self.entries.get((name, method))
    if not entry:
        entry = stats.StatsEntry(self, name, method)
        self.entries[(name, method)] = entry
    return entry

stats.RequestStats.get = monkey_get

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
            self.client.get(queue.pop())

class WebsiteUser(HttpLocust):
    # meaningless, because we're using full URLs, but require by Locust
    host = "https://www.hathitrust.org/"
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 1000
