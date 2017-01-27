# celery_blog.py

from celery import Celery
import requests

# created a celery instance
# The first argument to Celery is the name of the current module,
# this is needed so that names can be automatically generated,
# the second argument is the broker keyword argument which specifies
# the URL of the message broker we want to use
app = Celery('celery_blog', broker='redis://localhost:6379/0')

@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)

def func(urls):
    for url in urls:
        # the code is serialized and put in the message queue
        fetch_url.delay(url)

if __name__ == "__main__":
    func(["http://google.com", "https://amazon.in",
          "https://facebook.com", "https://twitter.com",
          "https://alexa.com"])