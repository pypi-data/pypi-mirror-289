Jh Scrapyd
==========

A preemptive scrapyd cluster built using Redis queues

* Free software: MIT license (including the work distributed under the Apache 2.0 license)
* Documentation: https://scrapyd.readthedocs.org/en/latest/

## Installation

scrapyd >= 1.4.3

Install with `pip` from PyPI:

```
pip install jh_scrapyd
```

## Configuration
editor scrapyd.conf
```
[scrapyd]
jobs_to_keep  = 20000
# Finished task queue
jobstorage    = scrapyd.jobstorage.SqliteJobStorage

# Queue system, queue related management
spiderqueue   = jh_scrapyd.spiderqueue.JsonRedisPriorityQueue

[services]
# The task is received and added to the queue
schedule.json = jh_scrapyd.webservice.JhSchedule

# Cancel queue task
cancel.json   = jh_scrapyd.webservice.JhCancel

[redis]
# Add Redis to configure celarclear
host = 127.0.0.1
port = 6379
db = 0
```