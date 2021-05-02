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

Hence, here, asynchronous (async) task scheduling via microservices provide an well offer to handle our issue!

## 🧪 What are async tasks and microservices?
TBA

## 💭 Use cases (aka. Real-life examples)
Maybe you might asking why we need this or what are the real-life examples? Actually, currently, several processes are going through in async way even we do not realize. 

**Here are the some cases:** 

_If you have more (and clear) examples, please just [reach me out](#-author--feedbackcontrubitons)._

<br>

<details>
    <summary>Use case #1 | Ordering a burger | <b>Literally real-life</b> 😊</summary>
    <p><br>Assume that you are hungry and looking forward to eating a burger!
    </p>
</details>

<br>

<details>
    <summary>Use case #2 | Basic example</summary>
    <p>Case Study 2</p>
</details>

<br>

<details>
    <summary>Use case #3 | Bioinformatics</summary>
    <p>Case Study 3</p>
</details>

<br><hr><br>

## 🎨 Architecture of the pipeline
TBA with images

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
0. Distill: Why do we need Flask, Celery, and Redis? (with McDonalds in Between). Retrieved 2 May 2021, from https://ljvmiranda921.github.io/notebook/2019/11/08/flask-redis-celery-mcdo/
1. An introduction to REST APIs. Retrieved 2 May 2021, from https://flaviocopes.com/rest-api/

## 🎈 Author & Feedback/Contribution
**About the author & developer**

- Furkan M. Torun
- Mail: [furkanmtorun@gmail.com](mailto:furkanmtorun@gmail.com) 
- Academia: [Google Scholar Profile](https://scholar.google.com/citations?user=d5ZyOZ4AAAAJ) 
- Website: furkanmtorun.github.io

Moreover, please do not hesitate to comment via `openning an issue via GitHub` if you have any suggestion or feedback!
