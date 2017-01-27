README.md

What is Celery:

Celery is a task processing system.

To do any network call in a request-response cycle. Server should respond immediately to any request it receives. If some other additional network call is required during a request-response cycle, it should be done outside of request-response cycle. eg: An activation email needs to be sent when user signs up on a site. Sending the email is a network call and might take 2-3 seconds. User should not be made to wait for these 2-3 seconds. So sending activation email should be done outside of request-response cycle. It can be achieved using celery.

Breaking a large job, consisting of several independent parts, into smaller tasks. eg: we want to read a user's FB timeline. FB provides different endpoints to get different kind of things. FB provides one endpoint to get pictures on a user's timelines, another endpoint to get posts on a user's timelines, another endpoint to get likes of a user etc. If you write a single function to sequentially hit 5 endpoints provided by FB and if network calls take 2 seconds at an average, then your function will take 10 seconds to complete. So you can split your work in 5 individual tasks(it's very easy to do as we will soon see), and let Celery handle the tasks. Celery can hit these 5 endpoints in parallel and you can get the response from all the endpoints within first 2 seconds.

Why use Celery:

We want service responses to be fast. So on user signup, server should send the response immediately and the actual job of sending the email should be sent to celery. Celery would be running in background, outside of request-response cycle and it can send the actual email.

We can use celery to make our scripts faster and to make better utilization of cpu. In the FB example I described earlier, we can go from 10 seconds to 2 seconds and also our cpu utilization would be higher if we use celery.

We can use celery to make our tasks more manageable. In our FB example, if everything were in a single function being executed sequentially and if an error occurred during fetching the second url, then other 3 urls wouldn't be hit. If all 5 urls were being executed in a different process, then getting an error in one process, wouldn't affect others. So tasks become more manageable if we use celery properly.

A celery worker can run multiple processes parallely. We want to hit all our urls parallely and not sequentially. So we need a function which can act on one url and we will run 5 of these functions parallely. So we wrote a celery task called fetch_url and this task can work with a single url. A celery task is just a function with decorator "app.task" applied to it.

When we say "fetch_url.delay(url)", the code is serialized and put in the message queue, which in our case is redis. Celery worker when running will read the serialized thing from queue, then deserialize it and then execute it.



