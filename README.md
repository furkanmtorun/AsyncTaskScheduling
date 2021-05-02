# Simple Pipeline for Asynchronous Task Scheduling in Python

## 📖 Table of Contents
- [Simple Pipeline for Asynchronous Task Scheduling in Python](#simple-pipeline-for-asynchronous-task-scheduling-in-python)
  - [📖 Table of Contents](#-table-of-contents)
  - [💡 TL;DR: What is this at all?](#-tldr-what-is-this-at-all)
  - [💢 Background knowledge](#-background-knowledge)
    - [🧪 What is async tasks and microservices?](#-what-is-async-tasks-and-microservices)
    - [💭 Use cases (aka. Real-life examples)](#-use-cases-aka-real-life-examples)
  - [🎨 Architecture of the pipeline](#-architecture-of-the-pipeline)
  - [🧵 Installation and Usage](#-installation-and-usage)
  - [💎 How the things go (aka. Results)?](#-how-the-things-go-aka-results)
  - [📘 References](#-references)
  - [🎈 Author & Feedback/Contrubitons](#-author--feedbackcontrubitons)

<br><hr><br>

## 💡 TL;DR: What is this at all?
TBA

## 💢 Background knowledge
TBA

### 🧪 What is async tasks and microservices?
TBA

### 💭 Use cases (aka. Real-life examples)
TBA for question "Why we need this?"

**Here are the some cases:**

<details>
    <summary>Case Study/Real-life example 1 | Basic</summary>
    <p>Case Study 1</p>
</details>

<details>
    <summary>Case Study/Real-life example 2 | Bioinformatics</summary>
    <p>Case Study 2</p>
</details>

<br><hr><br>

## 🎨 Architecture of the pipeline
TBA with images

<br>

## 🧵 Installation and Usage
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
1. An introduction to REST APIs. Retrieved 2 May 2021, from https://flaviocopes.com/rest-api/
2. 

## 🎈 Author & Feedback/Contrubitons
TBA