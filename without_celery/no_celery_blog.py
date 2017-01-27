# no_celery_blog.py

import requests
import time

def func(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
    print("It took", time.time() - start, "seconds")

if __name__ == "__main__":
    func(["http://google.com", "https://amazon.in", "https://facebook.com", 
          "https://twitter.com", "https://alexa.com"])