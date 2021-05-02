# Simple Pipeline for Asynchronous Task Scheduling

[![GitHub license](https://img.shields.io/badge/License-MIT-green)](https://github.com/furkanmtorun/AsyncTaskScheduling/blob/master/LICENSE) 

## 📖 Table of contents
- [Simple Pipeline for Asynchronous Task Scheduling](#simple-pipeline-for-asynchronous-task-scheduling)
  - [📖 Table of contents](#-table-of-contents)
  - [💡 TL;DR: What is this at all?](#-tldr-what-is-this-at-all)
  - [🧪 What are async tasks and microservices?](#-what-are-async-tasks-and-microservices)
  - [💭 Use cases (aka. Real-life examples)](#-use-cases-aka-real-life-examples)
  - [🎨 Architecture of the pipeline](#-architecture-of-the-pipeline)
  - [🧵 Installation & Running](#-installation--running)
  - [💎 How the things go (aka. Results)?](#-how-the-things-go-aka-results)
  - [📘 References](#-references)
  - [🎈 Author & Feedback/Contribution](#-author--feedbackcontribution)

<br><hr><br>

## 💡 TL;DR: What is this at all?
Together with advancements in computing capacity and increasing trend in working on the large scale datasets, in some projects, we might need to execute time-consuming and/or heavy functions upon the plenty of requests coming from the client side.

So, we shall to run them in background while still getting new requests from the client and finally, we should get back the result later once the process is done. 

Hence, here, asynchronous (`async`) task scheduling via microservices provide an well offer to handle our issue!

## 🧪 What are async tasks and microservices?

> Microservices

During designing a sofware pipeline, **Microservice Architecture**, where the applications, modules/functions work independently, has showed up for the last decade.

In this way, contast to monolithic architecture, the functional parts of your whole work are splitted into smaller units. Those smaller units are dedicated to work on a specific tasks and they do their job well! 
While working they do not really know what the others perform however they have a common port/way of communication where they are able to talk to each other. 

> Asynchronous (async) Programming  

TBA

## 💭 Use cases (aka. Real-life examples)
Maybe you might asking why we need this or what are the real-life examples? Actually, currently, several processes are going through in async way even we do not realize. 

**Here are the some real-life examples:** 

_If you have more (and/or clearer) examples, please just [reach me out](#-author--feedbackcontribution)._

<br>

<details>
    <summary>Use case #1 | Ordering a burger | <b>Literally real-life</b> 😊</summary>
    <p><br>Assume that you are starving and looking forward to eating a burger! <br><br>
    In this scenario, every customer is getting  reference number after their ordering. While the order is on its own way, the customers can just relax and control the dashboard for the status of their orders while the crew are working on other orders.
    <img src="https://ljvmiranda921.github.io/assets/png/flask-celery-redis/scene_03.svg">
    <br><br>
  Please, <a href="https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/"> check this awesome blog post here</a> to see the rest and to get the issue in the easiest way! (Even worthy to look at the cartoons!)
    </p>
</details>

<br>

<details>
    <summary>Use case #2 | Basic example</summary>
    <p>Think that we as a team or company are providing a form in our web page to our users or customers and they can fill the form. Supposing that we need a sort of computation which takes a lot of time once the form is filled. 
    <br></p>
    <img src="http://brunorocha.org/static/media/microservices/micro_services.png">
    <br><p> Now, in this scenario, our user will fill and submit the form, we will return that "OK, we got your request and will let you know". Meanwhile, we will perform needed calculation in background and once it's done, we will send an email containing the result of calculation to our user. Yey! <br><br>
    For this real-life example, you can find another repository and blog with its implementation <a href="http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html">here</a>.
    </p>
</details>
<br>

<details>
    <summary>Use case #3 | Bioinformatics/Computational Biology</summary>
    <p>Case Study 3</p>
</details>

<br><hr><br>

## 🎨 Architecture of the pipeline
TBA with images

For REST-API (using Swagger UI): Flask RESTPlus-API | See my post, https://github.com/furkanmtorun/Flask-RESTPlusAPI

<br>

## 🧵 Installation & Running
TBA with prompts

<br>

## 💎 How the things go (aka. Results)?
TBA with images

```
    # Redis
    redis-server --port 6380 --slaveof 127.0.0.1 6379

    # In the project folder for Flask UI
    celery worker -A flask_ui.celery_client -E --pool=solo -l info

    flower -A flask_ui.celery_client

    python flask_ui.py

    # In the project folder for REST-API
    celery worker -A flask_api.celery_client -E --pool=solo -l info

    flower -A flask_api.celery_client

    python flask_api.py
```

<br><hr><br>

## 📘 References

1. MIRANDA, L. (2019). Distill: Why do we need Flask, Celery, and Redis? (with McDonalds in Between). Retrieved 2 May 2021, from https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/
2. Copes, F. (2020). An introduction to REST APIs. Retrieved 2 May 2021, from https://flaviocopes.com/rest-api/
3. Smyth, P. (2018). Creating Web APIs with Python and Flask . Programming Historian. Retrieved from https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
4. Rocha, B. (2021). Microservices with Python, RabbitMQ and Nameko. Retrieved 2 May 2021, from http://brunorocha.org/python/microservices-with-python-rabbitmq-and-nameko.html



## 🎈 Author & Feedback/Contribution

**About the author & developer:**

- Furkan M. Torun
- Mail: [furkanmtorun@gmail.com](mailto:furkanmtorun@gmail.com) 
- Academia: [Google Scholar Profile](https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ) 
- Website: furkanmtorun.github.io

Moreover, please do not hesitate to comment via `openning an issue via GitHub` if you have any suggestion or feedback!
