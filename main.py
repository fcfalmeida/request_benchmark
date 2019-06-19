import requests
import sys

URL = sys.argv[1]
TOKEN = sys.argv[2]
NUMBER_REQUESTS = 100
sum = 0

for i in range(0, NUMBER_REQUESTS):
  time = requests.get(URL, cookies = {
    'token': TOKEN
  }).elapsed.total_seconds()

  time_ms = time * 1000

  print('Request {0} took {1}ms'.format(i + 1, time_ms))

  sum += time

average = (sum / NUMBER_REQUESTS) * 1000

print('Avg. request time: {0}ms'.format(int(average)))